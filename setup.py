#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from setuptools import setup


try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

try:
    with open("requirements.txt") as f:
        requirements = [x for x in [y.strip() for y in f.readlines()] if x]
except IOError:
    requirements = []

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                               "pip_init", "templates"))

template_files = [x for x in os.listdir(template_dir) if x.endswith(".j2")]

template_files = [("templates",
                   [os.path.join("templates", x)])
                  for x in template_files]
print template_files
setup(
    name="pip-init",
    version="0.1.0",
    description="pip-init to generate a base setup.py file",
    long_description=long_description,
    license='MIT',
    author="JuanPablo AJ, Jack Maney",
    author_email="jpabloaj@gmail.com, jackmaney@gmail.com",
    url="https://github.com/juanpabloaj/pip-init",
    packages=['pip_init'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'pip-init=pip_init:main',
        ],
    },
    # data_files=template_files,
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ]
)
