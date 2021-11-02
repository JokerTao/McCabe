#encoding=utf-8

import os
from setuptools import setup, find_packages

__version__ = '1.0' # 版本号
requirements = open('requirements.txt').readlines() # 依赖文件

setup(
    name = 'McCabeChecker', # 在pip中显示的项目名称
    version = __version__,
    author = 'LiPengTao',
    author_email = 'Joker_Taoy@163.com',
    url = '',
    description = 'McCabeChecker: Setup',
    packages = find_packages(exclude=["tests"]), # 项目中需要拷贝到指定路径的文件夹
    python_requires = '>=3.5.0',
    install_requires = requirements # 安装依赖
        )
