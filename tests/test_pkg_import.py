# -*- coding: utf-8 -*-

# SPDX-License-Identifier: MIT
# Copyright © 2021 André Santos

###############################################################################
# Imports
###############################################################################

from types import FunctionType

import chelone

###############################################################################
# Tests
###############################################################################

def test_import_was_ok():
    assert True

def test_pkg_has_version():
    assert hasattr(chelone, '__version__')
    assert isinstance(chelone.__version__, str)
    assert chelone.__version__ != ''

def test_pkg_has_main_function():
    assert hasattr(chelone, 'main')
    assert isinstance(chelone.main, FunctionType)
