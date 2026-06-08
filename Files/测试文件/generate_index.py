import os
import json
import datetime
from pathlib import Path

# ========== 路径修正（关键改动）==========
# 方案：全部使用仓库相对路径，本地和流水线共用一套配置
# 脚本位置假设在仓库根目录/docs/generate_index.py
BASE_DIR = Path("D:/desktop/curve_digitizer/Files")
OUTPUT_JSON_PATH = Path("D:/desktop/curve_digitizer/docs/index.json")

def get_file_size_str(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"

def get_file_info(file_rel_path: Path, base_path: Path):
    full_path = base_path / file_rel_path
    # 统一输出正斜杠URL路径（网站静态资源标准格式）
    rel_str = str(file_rel_path).replace("\\", "/")
    
    size_bytes = full_path.stat().st_size
    size_str = get_file_size_str(size_bytes)
    
    mtime = full_path.stat().st_mtime
    date_str = datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")
    
    name = full_path.name
    ext = name.split('.')[-1].lower() if '.' in name else ''
    
    # 文件夹路径，统一正斜杠
    folder_path = str(file_rel_path.parent).replace("\\", "/")
    folder = folder_path if folder_path != "." else ""
    
    # 本地测试用相对路径，上传 GitHub 不用改
    url = f"D:/desktop/curve_digitizer/Files/{rel_str}"

    # 线上 GitHub Pages 用（需要时再打开）
    # url = f"https://zilong7728.github.io/FileDir/Files/{rel_str}"
    
    return {
        "name": name,
        "ext": ext,
        "path": rel_str,
        "folder": folder,
        "size": size_str,
        "sizeBytes": size_bytes,
        "date": date_str,
        "url": url
    }

def scan_files(base_dir: Path):
    files = []
    if not base_dir.exists():
        print(f"错误：目录 '{base_dir}' 不存在")
        return files
    # rglob递归遍历所有文件
    for file_path in base_dir.rglob("*"):
        if file_path.is_file():
            rel_path = file_path.relative_to(base_dir)
            files.append(get_file_info(rel_path, base_dir))
    return files

def main():
    print(f"正在扫描目录: {BASE_DIR.resolve()}")
    all_files = scan_files(BASE_DIR)
    print(f"找到 {len(all_files)} 个文件")
    
    # 按修改时间倒序
    all_files.sort(key=lambda x: x["date"], reverse=True)
    
    # 自动创建父文件夹（docs不存在也不会报错）
    OUTPUT_JSON_PATH.parent.mkdir(exist_ok=True)
    with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(all_files, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 已生成索引文件: {OUTPUT_JSON_PATH.resolve()}")
    
    # 文件类型统计
    print("\n文件类型TOP10统计:")
    ext_count = {}
    for f in all_files:
        ext = f["ext"] if f["ext"] else "无扩展名"
        ext_count[ext] = ext_count.get(ext, 0) + 1
    for ext, count in sorted(ext_count.items(), key=lambda x: -x[1])[:10]:
        print(f"  .{ext}: {count} 个")

if __name__ == "__main__":
    main()