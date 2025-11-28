# jmcomic_pdf_cli/main.py
import sys
import shutil
from pathlib import Path
import re
import tempfile
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

import jmcomic



def list_dirs():
    return {p for p in Path(".").iterdir() if p.is_dir()}


def extract_number(filename: str) -> int:
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else 0


def webp_to_pdf(folder: Path, output_pdf: Path) -> bool:
    webp_files = sorted(
        folder.glob("*.webp"),
        key=lambda f: extract_number(f.name)
    )
    if not webp_files:
        print(f"⚠️ 警告：文件夹 {folder} 中无 .webp 文件", file=sys.stderr)
        return False

    print(f"🖼️  发现 {len(webp_files)} 张图片，正在生成 PDF...")

    with tempfile.TemporaryDirectory() as tmp_dir:
        jpg_paths = []
        for i, webp in enumerate(webp_files):
            try:
                with Image.open(webp) as img:
                    if img.mode != "RGB":
                        img = img.convert("RGB")
                    jpg_path = Path(tmp_dir) / f"{i:05d}.jpg"
                    img.save(jpg_path, "JPEG", quality=85)
                    jpg_paths.append(jpg_path)
            except Exception as e:
                print(f"❌ 转换失败 {webp}: {e}", file=sys.stderr)
                continue

        if not jpg_paths:
            return False

        c = canvas.Canvas(str(output_pdf))
        for jpg in jpg_paths:
            with Image.open(jpg) as img:
                w, h = img.size
                c.setPageSize((w, h))
                c.drawImage(ImageReader(str(jpg)), 0, 0, w, h)
                c.showPage()
        c.save()

    return True


def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("用法: jm <漫画ID>", file=sys.stderr)
        print("示例: jm 1156509", file=sys.stderr)
        sys.exit(1)

    comic_id = sys.argv[1]

    dirs_before = list_dirs()
    print(f"🔍 开始下载漫画 {comic_id}...")

    try:
        jmcomic.download_album(comic_id)
    except Exception as e:
        print(f"❌ 下载失败: {e}", file=sys.stderr)
        sys.exit(1)

    new_dirs = list_dirs() - dirs_before
    target_folder = None
    for folder in new_dirs:
        if any(folder.glob("*.webp")):
            target_folder = folder
            break

    if not target_folder:
        print("❌ 未找到包含 WebP 的新文件夹", file=sys.stderr)
        sys.exit(1)

    print(f"📁 目标文件夹: {target_folder}")

    output_pdf = Path(f"{comic_id}.pdf")
    if webp_to_pdf(target_folder, output_pdf):
        print(f"✅ PDF 已保存: {output_pdf.resolve()}")
        try:
            shutil.rmtree(target_folder)
            print(f"🗑️  已删除原始文件夹: {target_folder}")
        except Exception as e:
            print(f"⚠️  删除失败: {e}", file=sys.stderr)
    else:
        print("⚠️ PDF 生成失败，保留原始文件夹", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()