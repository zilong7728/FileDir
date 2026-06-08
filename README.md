# FileDir · 工程资料库
> 一个部署在 GitHub Pages 上的静态工程资料浏览器，无需后端，直接通过浏览器访问仓库中的文件。

**🔗 在线访问：** [https://zilong7728.github.io/FileDir/](https://zilong7728.github.io/FileDir/)
---
## ✨ 功能特性
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
## 🚀 使用方法
### 添加文件
1. 将文件放入仓库的 `Files/` 文件夹（支持任意层级子目录）。
2. 推送代码，GitHub Actions 会自动运行脚本更新目录索引。
3. 刷新页面即可看到新文件，分类和筛选按钮均会自动更新。
### 文件大小限制
| 上传方式        | 单文件上限         |
| --------------- | ------------------ |
| GitHub 网页上传 | 25 MB              |
| `git` 命令行    | 100 MB             |
| Git LFS         | 不限（需额外配置） |
> **⚠️ 注意：** 避免将文件夹命名为带扩展名的形式（如 `schematics.pdf`），否则系统可能无法正确识别为文件夹。
---
## 💡 如何 Fork 并打造自己的资料库
本项目采用“代码与数据分离”的架构设计，`main` 分支为纯净模板。如果你想拥有自己的文件导航页：
1. **Fork 本仓库**：你将获得一个干净的 `main` 模板分支（不包含原作者的私人资料）。
2. **开启 Actions 权限**：进入仓库 `Settings` -> `Actions` -> `General`，将 Workflow permissions 设置为 **Read and write permissions** 并保存。
3. **设置 GitHub Pages**：进入 `Settings` -> `Pages`，将 Source 分支设置为 `main`，目录必须选择 **`/ (root)`**。
4. **上传资料**：直接将你的文件上传到 `Files/` 文件夹中，机器人会自动为你生成专属索引并刷新网页！
---
## 📁 仓库结构
```text
FileDir/
├── .github/workflows/
│   └── static.yml            # GitHub Actions：自动化构建工作流配置
├── docs/                     # 核心逻辑与数据目录
│   ├── generate_index.py     # Python 脚本：扫描目录并生成 JSON 索引
│   └── index.json            # 索引数据：由脚本自动生成
├── Files/                    # 资料库：存放所有工程资料（可任意组织子目录）
├── index.html                # 前端入口：纯原生实现，直接读取 docs/index.json
└── README.md
```
---
## ⚙️ 工作原理
彻底排除了传统的页面抓取模式。当仓库的 `Files/` 目录发生变动并推送到 GitHub 时，**GitHub Actions** 会自动触发 `docs/generate_index.py` 脚本，极速扫描最新的文件结构，并生成轻量化的 `index.json` 数据文件存入 `docs/` 目录。
前端页面 `index.html` 部署在根目录，加载时直接 `fetch` 位于 `docs/index.json` 的数据文件，在本地瞬间完成目录树构建、分类、搜索与渲染，全程无需任何后端服务器介入，速度极快且高度稳定。

---
## 🛠️ 技术栈与致谢
* **前端实现**：纯原生 HTML / CSS / JavaScript，无框架依赖，无构建步骤
* **数据生成**：Python (自动化文件树遍历与信息提取)
* **UI 资源**：[Tabler Icons](https://tabler-icons.io/) 图标、[IBM Plex Mono](https://fonts.google.com/specimen/IBM+Plex+Mono) 字体
* **托管服务**：GitHub Pages + GitHub Actions
**🙌 特别致谢 (Credits)：**
* **灵感来源**：本项目的设计灵感与核心理念深受开源项目 [github-pages-directory-listing](https://github.com/jayanta525/github-pages-directory-listing) 的启发。在此向原作者表示由衷的感谢。
* **AI 赋能**：本项目的整个代码重构、双分支隔离架构设计、以及全套核心功能（目录树、模糊搜索、快捷统计等）的二次开发迭代，均在 **Gemini / Claude / ChatGPT** 等前沿人工智能模型的深度辅助下开发完成。
---
## ⚖️ 侵权声明
本仓库收录的资料均来自公开渠道，仅供个人学习参考。如有侵权，请 [提交 Issue](https://github.com/zilong7728/FileDir/issues) 联系删除。
