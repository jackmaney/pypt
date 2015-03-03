#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pypt._version import __version__


try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

try:
    with open("requirements.txt") as f:
        requirements = [x for x in [y.strip() for y in f.readlines()] if x]
except IOError:
    requirements = []

setup(
    name="PyPT",
    version=__version__,
    description="Python Package Tools",
    long_description=long_description,
    license='MIT',
    author="Jack Maney",
    author_email="jackmaney@gmail.com",
    url="https://github.com/jackmaney/pypt",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'pypt=pypt:main',
        ],
    },
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ]
)
