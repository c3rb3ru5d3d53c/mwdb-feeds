#!/usr/bin/env python

import os
from glob import glob
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__author__  = 'c3r3b3ru5'
__version__ = '1.0.0'

def get_requirements(default):
    result = []
    requirement_files = [y for x in os.walk('modules') for y in glob(os.path.join(x[0], 'requirements.txt'))]
    requirement_files.append(default)
    for requirement_file in requirement_files:
        f = open(requirement_file, "r")
        result.extend(f.read().splitlines())
    return list(dict.fromkeys(result))

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="mwdb-feeds",
    version=__version__,
    maintainer=__author__,
    description='A Modular MWDB Utility to Collect Fresh Malware Samples',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=get_requirements('requirements.txt'),
    scripts=['mwdb-feeds'],
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
)