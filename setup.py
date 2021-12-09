# -*- coding: utf-8 -*-

# SPDX-License-Identifier: MIT
# Copyright © 2021 André Santos

###############################################################################
# Imports
###############################################################################

from pathlib import Path
from setuptools import setup, find_packages
import regex

###############################################################################
# Constants
###############################################################################

PROJECT = 'chelone'
PYTHON_PKG = 'chelone'
HERE = Path(__file__).parent
SRC = str(HERE / 'src')

###############################################################################
# Utility
###############################################################################

# Utility function to read the README, etc..
# Used for the long_description and other fields.
def read(filename):
    return (HERE / filename).read_text(encoding='utf-8')

def read_version():
    filepath = HERE / 'src' / PYTHON_PKG / '__init__.py'
    init = filepath.read_text(encoding='utf-8')
    version, = regex.findall(r"__version__ = '(.*)'", init)
    return version

###############################################################################
# Setup
###############################################################################

__version__ = read_version()

requirements = [r for r in read(HERE / 'requirements.txt').splitlines() if r]

long_description = (HERE / 'README.md').read_text(encoding='utf-8')

setup(
    name             = PROJECT,
    version          = __version__,
    description      = 'Variability analysis tool for ROS systems',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url              = 'https://github.com/git-afsantos/' + PROJECT,
    author           = u'André Santos',
    author_email     = 'haros.framework@gmail.com',
    license          = 'MIT',
    keywords         = 'ros, variability, software product lines, feature models',
    packages         = find_packages(where=SRC),
    package_dir      = {'': SRC},
    package_data     = {}, # {PYTHON_PKG: ['dir/*.file']},
    classifiers      = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only'
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance'
    ],
    entry_points     = {'console_scripts': [f'{PROJECT}={PYTHON_PKG}:main']},
    python_requires  = '>=3.6, <4',
    install_requires = requirements,
    extras_require   = {},
    # zip_safe         = False,
    project_urls     = {
        'Source': 'https://github.com/git-afsantos/' + PROJECT + '/',
        'Tracker': 'https://github.com/git-afsantos/' + PROJECT + '/issues',
        # 'Say Thanks!': 'http://saythanks.io/to/haros-framework',
    },
)
