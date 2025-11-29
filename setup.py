# setup.py
from setuptools import setup, find_packages

setup(
    name="jm2pdf",
    version="0.1.0",
    packages=find_packages(), 
    install_requires=[
        "jmcomic>=2.0",
        "Pillow>=9.0",
        "reportlab>=3.6",
    ],
    entry_points={
        "console_scripts": [
            "jm=jm2pdf.main:main",
        ],
    },
)
