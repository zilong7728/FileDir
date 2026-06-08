# FileDir · 工程资料库

> 一个部署在 GitHub Pages 上的静态工程资料浏览器，无需后端，直接通过浏览器访问仓库中的文件。

**在线访问：** https://zilong7728.github.io/FileDir/

---

## 功能特性

- **IDE 风格目录树** — 左侧侧边栏以可折叠树形结构展示全部文件夹与文件，支持逐级展开/收起
- **面包屑导航** — 顶部路径栏显示当前所在目录层级，每一级均可点击跳转
- **全局文件视图** — 一键切换至「全部文件 (全局)」模式，跨目录浏览所有文件
- **动态扩展名分类** — 侧边栏按文件扩展名自动生成分类标签，无需手动维护
- **顶部快捷筛选** — 自动统计文件数量，将出现最多的 Top 5 扩展名生成快捷筛选按钮
- **文件名模糊搜索** — 支持按字符顺序匹配，跨目录搜索
- **文件预览面板** — 点击文件展开右侧详情，图片直接显示缩略图，PDF 可跳转在线预览
- **最近更新栏** — 底部显示最新修改的文件快捷入口
- **深色模式** — 跟随系统自动切换
- **响应式布局** — 兼容移动端（侧边栏自动隐藏）

---

## 使用方法

### 添加文件

1. 将文件放入仓库的 `Files/` 文件夹（支持任意层级子目录）
2. 推送到 `main` 分支，GitHub Actions 自动更新目录索引
3. 刷新页面即可看到新文件，分类和筛选按钮均自动更新

### 文件大小限制

| 上传方式 | 单文件上限 |
|---|---|
| GitHub 网页上传 | 25 MB |
| `git` 命令行 | 100 MB |
| Git LFS | 不限（需额外配置） |

> **注意：** 避免将文件夹命名为带扩展名的形式（如 `schematics.pdf`），否则 GitHub Pages 目录列表可能无法正确识别为文件夹。

---

## 仓库结构

```
FileDir/
├── .github/
│   └── workflows/      # GitHub Actions：自动生成目录索引
├── Files/              # 存放所有工程资料（可任意组织子目录）
├── index.html          # 前端页面（单文件，纯原生，无需构建）
└── README.md
```

---

## 工作原理

页面加载时，通过 `fetch` 递归抓取 GitHub Pages 生成的目录索引页（`index.html` 列表），解析出文件名、路径、大小、修改时间等信息，在本地完成目录树构建、分类、搜索与渲染，无需任何后端服务。

---

## 技术栈

- 纯原生 HTML / CSS / JavaScript，无框架依赖，无构建步骤
- [Tabler Icons](https://tabler-icons.io/) — 图标
- [IBM Plex Mono](https://fonts.google.com/specimen/IBM+Plex+Mono) — 字体
- GitHub Pages — 静态托管
- GitHub Actions — 自动生成目录索引（[github-pages-directory-listing](https://github.com/jayanta525/github-pages-directory-listing)）

---

## 侵权声明

本仓库收录的资料均来自公开渠道，仅供个人学习参考。如有侵权，请 [提交 Issue](https://github.com/zilong7728/FileDir/issues) 联系删除。
