# JMComic PDF Plugin

一个轻量级 Python 插件，用于在使用 [JMComic-Crawler-Python](https://github.com/hect0x7/JMComic-Crawler-Python) 下载漫画后，**自动将 WebP 图片合并为 PDF**，并清理原始文件夹。

> 输入 `jm 1156509` → 自动下载 → 转 PDF → 删除原图文件夹  
> 输出：`1156509.pdf`

---

## ✨ 功能特点

- ✅ 通过目录快照精准识别新下载的漫画文件夹（不依赖文件名）
- ✅ 自动按数字顺序排序图片（支持 `1.webp`, `02.webp`, `100.webp`）
- ✅ 保留原始图片尺寸生成高质量 PDF
- ✅ PDF 生成成功后自动删除 WebP 原图文件夹，节省空间
- ✅ 完全基于 `jmcomic` Python API，无需命令行调用

---

## 🚀 安装

```bash
# 1. 安装依赖
pip install jmcomic pillow reportlab

# 2. 安装本工具（在项目根目录执行）
pip install -e .
💡 首次使用前请确保已配置好 jmcomic（如账号、下载路径等）。

▶️ 使用方法
```bash
jm <漫画ID>
```
示例：
```bash
jm 1156509
```
执行后：

自动调用 jmcomic.download_album(1156509)
在当前目录生成 1156509.pdf
原始 WebP 文件夹被自动删除
⚙️ 依赖说明
包    用途
jmcomic    漫画下载核心库
Pillow    读取和转换 WebP 图片
reportlab    生成 PDF 文档
详见 requirements.txt

📜 许可证
本项目采用 MIT License —— 免费用于个人或商业项目。
