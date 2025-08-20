# SPDX-License-Identifier: MIT
# Copyright © 2021 André Santos

"""
Module that contains the command line program.

Why does this file exist, and why not put this in __main__?

  In some cases, it is possible to import `__main__.py` twice.
  This approach avoids that. Also see:
  https://click.palletsprojects.com/en/5.x/setuptools/#setuptools-integration

Some of the structure of this file came from this StackExchange question:
  https://softwareengineering.stackexchange.com/q/418600
"""

###############################################################################
# Imports
###############################################################################

from typing import Any, Final

import argparse
from collections.abc import Mapping, Sequence
import sys

from bakeapy import __version__ as current_version

###############################################################################
# Constants
###############################################################################

PROG: Final[str] = 'bake-a-py'

###############################################################################
# Argument Parsing
###############################################################################


def parse_arguments(argv: Sequence[str] | None) -> dict[str, Any]:
    msg = 'A short description of the project.'
    parser = argparse.ArgumentParser(prog=PROG, description=msg)

    parser.add_argument(
        '--version',
        dest='version',
        action='version',
        version=f'{PROG} {current_version}',
        help='Prints the program version.',
    )

    parser.add_argument(
        'args', metavar='ARG', nargs=argparse.ZERO_OR_MORE, help='An argument for the program.'
    )

    args = parser.parse_args(args=argv)
    return vars(args)


###############################################################################
# Setup
###############################################################################


def load_configs(args: Mapping[str, Any]) -> dict[str, Any]:
    try:
        config: dict[str, Any] = {}
        # with open(args['config_path'], 'r') as file_pointer:
        # yaml.safe_load(file_pointer)

        # arrange and check configs here

        return config
    except Exception as err:
        # log or raise errors
        print(err, file=sys.stderr)
        if str(err) == 'Really Bad':
            raise err

        # Optional: return some sane fallback defaults.
        sane_defaults: dict[str, Any] = {}
        return sane_defaults


###############################################################################
# Commands
###############################################################################


def do_real_work(args: Mapping[str, Any], configs: Mapping[str, Any]) -> None:
    print(f'Arguments: {args}')
    print(f'Configurations: {configs}')


###############################################################################
# Entry Point
###############################################################################


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_arguments(argv)

    try:
        # Load additional config files here, e.g., from a path given via args.
        # Alternatively, set sane defaults if configuration is missing.
        config = load_configs(args)
        do_real_work(args, config)

    except KeyboardInterrupt:
        print('Aborted manually.', file=sys.stderr)
        return 1

    except Exception as err:
        # In real code the `except` would probably be less broad.
        # Turn exceptions into appropriate logs and/or console output.

        import traceback

        print('An unhandled exception crashed the application!', err)
        traceback.print_exc()

        # Non-zero return code to signal error.
        # It can, of course, be more fine-grained than this general code.
        return 1

    return 0  # success
