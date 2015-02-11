#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pip_create._version import __version__


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
    name="pip-create",
    version=__version__,
    description="Tools to create a Python distribution for use with pip",
    long_description=long_description,
    license='MIT',
    author="Jack Maney",
    author_email="jackmaney@gmail.com",
    url="https://github.com/jackmaney/pip-create",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'pip-create=pip_create:main',
        ],
    },
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ]
)
