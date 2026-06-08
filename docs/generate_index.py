import os
import json
import datetime
from pathlib import Path

BASE_DIR = "Files"
OUTPUT_JSON = "docs/index.json"

def get_file_size_str(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"

def get_file_info(file_path, base_dir):
    full_path = os.path.join(base_dir, file_path)
    rel_path = file_path.replace("\\", "/")
    
    size_bytes = os.path.getsize(full_path)
    size_str = get_file_size_str(size_bytes)
    
    mtime = os.path.getmtime(full_path)
    date_str = datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")
    
    name = os.path.basename(file_path)
    ext = name.split('.')[-1].lower() if '.' in name else ''
    
    # 文件夹路径：相对于 Files/ 的路径，不加前导斜杠，根目录为 ""（空字符串）
    folder_path = os.path.dirname(file_path).replace("\\", "/")
    # 如果文件就在 Files/ 根目录下，folder 设为 ""；否则设为不带前导斜杠的路径
    folder = folder_path if folder_path else ""
    
    # 【核心修改点 👇】
    # 丢弃绝对链接，直接采用相对于 index.html 的相对路径
    url = f"./Files/{rel_path}"
    
    return {
        "name": name,
        "ext": ext,
        "path": rel_path,
        "folder": folder,
        "size": size_str,
        "sizeBytes": size_bytes,
        "date": date_str,
        "url": url
    }

def scan_files(base_dir):
    files = []
    base_path = Path(base_dir)
    if not base_path.exists():
        print(f"错误：目录 '{base_dir}' 不存在")
        return files
    for file_path in base_path.rglob("*"):
        if file_path.is_file():
            rel_path = file_path.relative_to(base_path)
            files.append(get_file_info(str(rel_path), base_dir))
    return files

def main():
    print(f"正在扫描目录: {BASE_DIR}")
    all_files = scan_files(BASE_DIR)
    print(f"找到 {len(all_files)} 个文件")
    
    all_files.sort(key=lambda x: x["date"], reverse=True)
    
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(all_files, f, ensure_ascii=False, indent=2)
    
    print(f"已生成 {OUTPUT_JSON}")
    
    print("\n文件类型统计:")
    ext_count = {}
    for f in all_files:
        ext = f["ext"] if f["ext"] else "无扩展名"
        ext_count[ext] = ext_count.get(ext, 0) + 1
    for ext, count in sorted(ext_count.items(), key=lambda x: -x[1])[:10]:
        print(f"  .{ext}: {count} 个")

if __name__ == "__main__":
    main()
