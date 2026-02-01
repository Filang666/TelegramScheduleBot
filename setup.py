#!/usr/bin/env python3
"""
Setup file for Telegram Schedule Bot
"""

import re
from pathlib import Path

from setuptools import find_packages, setup


# Read the README file for long description
def read_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Telegram bot for school schedule management"


# Get version from src/__init__.py
def get_version():
    version_file = Path("src/__init__.py")
    if version_file.exists():
        with open(version_file, "r", encoding="utf-8") as f:
            content = f.read()
            match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', content)
            if match:
                return match.group(1)
    return "1.0.0"


# Get requirements from requirements.txt
def get_requirements():
    requirements_file = Path("requirements.txt")
    if requirements_file.exists():
        with open(requirements_file, "r", encoding="utf-8") as f:
            return [
                line.strip() for line in f if line.strip() and not line.startswith("#")
            ]
    return []


setup(
    name="telegram-schedule-bot",
    version=get_version(),
    description="Telegram bot for managing and distributing school schedules",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    author=".nixnix",
    author_email="timurovichroman@gmail.com",
    url="https://github.com/Filang666/telegram-schedule-bot",
    license="MIT",
    # Package discovery
    packages=find_packages(include=["src", "src.*"]),
    package_dir={"": "."},
    include_package_data=True,
    # Dependencies
    install_requires=get_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.0.0",
            "flake8>=6.0.0",
            "black>=23.0.0",
            "mypy>=1.0.0",
            "pre-commit>=3.0.0",
            "tox>=4.0.0",
        ],
    },
    # Python requirements
    python_requires=">=3.9",
    # Entry points
    entry_points={
        "console_scripts": [
            "schedule-bot=src.aiogram_run:main",
            "schedule-parser=src.parsing:main",
        ],
    },
    # Classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Russian",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Education",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
    # Project keywords
    keywords=[
        "telegram",
        "bot",
        "schedule",
        "school",
        "education",
        "aiogram",
        "automation",
    ],
    # Project URLs
    project_urls={
        "Documentation": "https://github.com/Filang666/telegram-schedule-bot/wiki",
        "Source": "https://github.com/Filang666/telegram-schedule-bot",
        "Tracker": "https://github.com/Filang666/telegram-schedule-bot/issues",
    },
    zip_safe=False,
)
