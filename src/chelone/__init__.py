# -*- coding: utf-8 -*-

# SPDX-License-Identifier: MIT
# Copyright © 2021 André Santos

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version('chelone')
except PackageNotFoundError:
    # package is not installed
    __version__ = 'unknown'

def main() -> int:
    print('Hello, world!')
    return 0
