import os
import json
import datetime
from pathlib import Path

BASE_DIR = "Files"
OUTPUT_JSON = "index.json"

def get_file_size_str(size_bytes):
    """将字节数转换为人类可读格式"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"

def get_file_info(file_path, base_dir):
    """提取单个文件的元数据"""
    full_path = os.path.join(base_dir, file_path)
    rel_path = file_path.replace("\\", "/")
    
    # 获取文件大小
    size_bytes = os.path.getsize(full_path)
    size_str = get_file_size_str(size_bytes)
    
    # 获取修改时间
    mtime = os.path.getmtime(full_path)
    date_str = datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")
    
    # 提取文件名和扩展名
    name = os.path.basename(file_path)
    ext = name.split('.')[-1].lower() if '.' in name else ''
    
    # 提取文件夹路径（去掉 Files/ 前缀）
    folder = os.path.dirname(file_path).replace("\\", "/")
    if folder == "":
        folder = "/"
    else:
        folder = "/" + folder
    
    # 构建完整URL（部署后的访问地址）
    # 注意：实际URL需要根据你的GitHub Pages地址调整
    url = f"https://zilong7728.github.io/FileDir/{rel_path}"
    
    return {
        "name": name,
        "ext": ext,
        "cat": "Other",  # 分类由前端根据扩展名决定，这里留空或前端覆盖
        "path": rel_path,
        "folder": folder,
        "size": size_str,
        "sizeBytes": size_bytes,
        "date": date_str,
        "days": 0,  # 前端会重新计算
        "url": url,
        "isDir": False
    }

def scan_files(base_dir):
    """递归扫描目录，返回文件列表"""
    files = []
    base_path = Path(base_dir)
    
    if not base_path.exists():
        print(f"错误：目录 '{base_dir}' 不存在")
        return files
    
    for file_path in base_path.rglob("*"):
        if file_path.is_file():
            # 获取相对于 base_dir 的路径
            rel_path = file_path.relative_to(base_path)
            files.append(get_file_info(str(rel_path), base_dir))
    
    return files

def main():
    print(f"正在扫描目录: {BASE_DIR}")
    all_files = scan_files(BASE_DIR)
    print(f"找到 {len(all_files)} 个文件")
    
    # 按修改时间排序，最新的在前（可选）
    all_files.sort(key=lambda x: x["date"], reverse=True)
    
    # 输出到 JSON
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(all_files, f, ensure_ascii=False, indent=2)
    
    print(f"已生成 {OUTPUT_JSON}")
    
    # 同时生成一个简单的统计信息
    print("\n文件类型统计:")
    ext_count = {}
    for f in all_files:
        ext = f["ext"] if f["ext"] else "无扩展名"
        ext_count[ext] = ext_count.get(ext, 0) + 1
    for ext, count in sorted(ext_count.items(), key=lambda x: -x[1])[:10]:
        print(f"  .{ext}: {count} 个")

if __name__ == "__main__":
    main()
