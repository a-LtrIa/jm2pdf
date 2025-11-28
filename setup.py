# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="jmcomic-pdf-cli",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="一键下载 JM 漫画并转为 PDF",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourname/jmcomic-pdf-cli",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "jmcomic>=2.0",
        "Pillow>=9.0",
        "reportlab>=3.6",
    ],
    entry_points={
        "console_scripts": [
            "jm=jmcomic_pdf_cli.main:main",  # 关键！注册 jm 命令
        ],
    },
)