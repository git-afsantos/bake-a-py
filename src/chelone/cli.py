# SPDX-License-Identifier: MIT
# Copyright © 2021 André Santos

'''
Module that contains the command line program.

Why does this file exist, and why not put this in __main__?

  In some cases, it is possible to import `__main__.py` twice.
  This approach avoids that. Also see:
  https://click.palletsprojects.com/en/5.x/setuptools/#setuptools-integration
'''

###############################################################################
# Imports
###############################################################################

import argparse
from typing import Any, Dict, List

from chelone import __version__ as current_version

###############################################################################
# Argument Parsing
###############################################################################

def parse_arguments(args: List[str]) -> Dict[str, Any]:
    msg = 'A short description of the project.'
    parser = argparse.ArgumentParser(description=msg)

    parser.add_argument('--version', dest='version', action='store_true',
                        help='Prints the program version.')

    parser.add_argument('args', metavar='ARG', nargs=argparse.ZERO_OR_MORE,
                        help='An argument for the program.')

    args = parser.parse_args(args=args)
    args = vars(args)
    return args


###############################################################################
# Entry Point
###############################################################################

def main(argv: List[str]) -> int:
    args = parse_arguments(argv)
    print(args)
    if args['version']:
        print(f'Version: {current_version}')
    return 0
