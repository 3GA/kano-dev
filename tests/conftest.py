# conftest.py
#
# Copyright (C) 2017 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# TODO: Description


import os
import sys
import shutil
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from tests.fixtures.app_args import *
from tests.fixtures.apt_sources import *
from tests.fixtures.dropbear_ssh_config import *

from kano_dev.paths import TEST_TEMP_DIR


REASON_USES_SED = '' \
    'Function uses [sed] internally which behaves differently on other' \
    ' platforms - Mac OS for instance. It is intented for Kano OS only.'

REASON_REQUIRES_KANO_OS = '' \
    'Function makes system wide changes in Kano OS and was designed to' \
    ' be executed in that environment, e.g. systemd, config files, etc.'

REASON_MISSING_PYPKG = '' \
    'Function requires extra python modules that are not installed' \
    ' in this environment.'


def pytest_namespace():
    """ TODO: Description """
    return {
        # Strings for tests marked with skipif.
        'REASON_USES_SED': REASON_USES_SED,
        'REASON_REQUIRES_KANO_OS': REASON_REQUIRES_KANO_OS,
        'REASON_MISSING_PYPKG': REASON_MISSING_PYPKG,

        # General purpose utility functions used only by tests.
        'is_kano_os': is_kano_os,
        'is_pypkg_installed': is_pypkg_installed,
    }


def is_kano_os():
    """
    TODO: Description
    """
    return os.path.exists('/etc/kanux_version')


def is_pypkg_installed(modules):
    """
    TODO: Description
    """
    all_installed = True

    for module in modules:
        try:
            print module
            importlib.import_module(module)
        except ImportError:
            print 'Missing dependency: [{}] python module.'.format(module)
            all_installed = False

    return all_installed


@pytest.fixture(scope='session')
def real_temp_dir():
    """
    TODO: Description
    """
    try:
        os.mkdir(TEST_TEMP_DIR)
    except OSError:
        # Directory already exists.
        pass

    yield

    # Clean up code, remove the temp directory altogether.
    if os.path.exists(TEST_TEMP_DIR):
        shutil.rmtree(TEST_TEMP_DIR)
