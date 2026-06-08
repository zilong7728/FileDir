# FileDir · 工程资料库

一个部署在 GitHub Pages 上的静态工程资料浏览器，无需后端，直接通过浏览器访问仓库中的文件。

🔗 **在线访问**：[https://zilong7728.github.io/FileDir/](https://zilong7728.github.io/FileDir/)

## ✨ 功能特性

* **IDE 风格目录树** — 左侧侧边栏以可折叠树形结构展示全部文件夹与文件，支持逐级展开/收起
* **面包屑导航** — 顶部路径栏显示当前所在目录层级，每一级均可点击跳转
* **全局文件视图** — 一键切换至「全部文件 (全局)」模式，跨目录浏览所有文件
* **动态扩展名分类** — 侧边栏按文件扩展名自动生成分类标签，无需手动维护
* **顶部快捷筛选** — 自动统计文件数量，将出现最多的 Top 5 扩展名生成快捷筛选按钮
* **文件名模糊搜索** — 支持按字符顺序匹配，跨目录搜索
* **文件预览面板** — 点击文件展开右侧详情，图片直接显示缩略图，PDF 可跳转在线预览
* **最近更新栏** — 底部显示最新修改的文件快捷入口
* **深色/浅色模式** — 跟随系统自动切换
* **响应式布局** — 兼容移动端（侧边栏自动隐藏）

## 🚀 使用方法

### 添加文件
1. 将文件放入仓库的 `Files/` 文件夹（支持任意层级子目录）。
2. 推送到 `main` 分支，GitHub Actions 会自动运行脚本更新目录索引。
3. 刷新页面即可看到新文件，分类和筛选按钮均会自动更新。

### 文件大小限制

| 上传方式 | 单文件上限 |
| --- | --- |
| GitHub 网页上传 | 25 MB |
| Git 命令行推送 | 100 MB |
| Git LFS | 不限（需额外配置） |

> **⚠️ 注意：** 避免将文件夹命名为带扩展名的形式（如 `schematics.pdf`），否则系统可能无法正确将其识别为文件夹。

## 📁 仓库结构

```text
FileDir/
├── .github/
│   └── workflows/
│       └── update-index.yml   # GitHub Actions：自动化工作流配置
├── Files/                     # 存放所有工程资料（可任意组织子目录）
├── docs/                      # 核心页面与脚本目录（供 Pages 读取）
│   ├── generate_index.py      # Python 脚本：扫描 Files 并生成数据
│   ├── index.html             # 前端页面：单文件纯原生实现
│   └── index.json             # 索引数据：由脚本自动生成
└── README.md

```

## ⚙️ 工作原理

当仓库的 `Files/` 目录发生变动并推送到 GitHub 时，**GitHub Actions** 会自动触发 `generate_index.py` 脚本，扫描最新的文件结构并生成轻量化的 `index.json` 数据文件。前端页面 `index.html` 加载时，直接读取该 JSON 文件，在本地极速完成目录树构建、分类、搜索与渲染，全程无需任何后端服务器介入。

## 🛠️ 技术栈

* **前端实现**：纯原生 HTML / CSS / JavaScript，无框架依赖，无构建步骤。
* **数据生成**：Python (自动化文件树遍历与信息提取)。
* **自动化与托管**：GitHub Actions + GitHub Pages。
* **UI 资源**：Tabler Icons 图标库、IBM Plex Mono 字体。

## 💡 如何 Fork 并部署自己的页面

如果你想 Fork 本项目搭建自己的文件索引页，请在 Fork 后完成以下三步配置：

1. **开启 Actions 自动化工作流**：
* 点击仓库顶部的 **Actions** 标签页。
* 点击绿色按钮 `I understand my workflows, go ahead and enable them`。


2. **授予工作流读写权限**（用于让机器人自动提交 JSON 索引）：
* 进入仓库的 **Settings** -> **Actions** -> **General**。
* 滚动到页面底部的 **Workflow permissions** 区域。
* 勾选 **Read and write permissions**，并点击 **Save**。


3. **配置 GitHub Pages 静态网页**：
* 进入仓库的 **Settings** -> **Pages**。
* 在 **Build and deployment** 下方的 **Source** 保持选择 `Deploy from a branch`。
* 在 **Branch** 处，第一个下拉菜单选择主分支（通常是 `main`），**第二个下拉菜单选择 `/docs**`。
* 点击 **Save**。稍等几分钟，刷新页面即可看到你的专属工程资料浏览器。


## ⚖️ 侵权声明

本仓库收录的资料均来自公开渠道，仅供个人学习参考。如有侵权，请提交 Issue 联系删除。

