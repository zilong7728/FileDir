import os
import json

BASE_DIR = "Files"

def scan_dir(path):
    tree = {}

    for root, dirs, files in os.walk(path):
        rel = os.path.relpath(root, path)
        if rel == ".":
            rel = ""

        node = tree
        if rel:
            parts = rel.split(os.sep)
            for p in parts:
                node = node.setdefault(p, {"_files": {}, "_dirs": {}})

        for d in dirs:
            node.setdefault(d, {"_files": {}, "_dirs": {}})

        for f in files:
            node.setdefault("_files", {})[f] = os.path.join(root, f).replace("\\", "/")

    return tree

index = scan_dir(BASE_DIR)

with open("index.json", "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)