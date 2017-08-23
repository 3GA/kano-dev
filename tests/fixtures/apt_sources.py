# apt_sources.py
#
# Copyright (C) 2017 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# TODO: Description


import os
import pytest
import textwrap

from kano_dev.paths import TEST_TEMP_DIR, KANO_LIST_NAME, RASPI_LIST_NAME


DEFAULT_KANO_LIST = textwrap.dedent("""
    #
    # Kano Official Package Repository
    # Key:
    #   curl -L http://repo.kano.me/archive-jessie/repo.gpg.key | apt-key add -
    #
    deb http://repo.kano.me/archive-jessie/ release main
    deb http://repo.kano.me/archive-jessie/ release-urgent main

    #
    # Kano Development Repository
    # Contains the newest unstable/untested packages
    #
    # Key:
    #   curl -L http://repo.kano.me/archive-jessie/repo.gpg.key | apt-key add -
    #
    # WARNING: Use at your own risk!
    #
    # deb http://dev.kano.me/archive-jessie/ devel main
    """)

DEFAULT_RASPI_LIST = textwrap.dedent("""
    #
    # Mirrored version of Raspberry Pi Foundation's repository
    # Key:
    #   curl -L http://repo.kano.me/raspberrypi/raspberrypi.gpg.key | apt-key add -
    #
    # The original repo is avaiable at:
    #   http://archive.raspberrypi.org/debian/
    #
    deb http://repo.kano.me/raspberrypi-jessie/ jessie main ui
    """)


@pytest.fixture(scope='function')
def kano_list(real_temp_dir):
    """
    # TODO: Description
    """
    kano_list_path = os.path.abspath(os.path.join(TEST_TEMP_DIR, KANO_LIST_NAME))

    with open(kano_list_path, 'w') as kano_list:
        kano_list.write(DEFAULT_KANO_LIST)

    yield kano_list

    # Clean up code, remove the file altogether.
    if os.path.exists(kano_list_path):
        os.remove(kano_list_path)


@pytest.fixture(scope='function')
def raspi_list(real_temp_dir):
    """
    # TODO: Description
    """
    raspi_list_path = os.path.abspath(os.path.join(TEST_TEMP_DIR, RASPI_LIST_NAME))

    with open(raspi_list_path, 'w') as raspi_list:
        raspi_list.write(DEFAULT_RASPI_LIST)

    yield raspi_list

    # Clean up code, remove the file altogether.
    if os.path.exists(raspi_list_path):
        os.remove(raspi_list_path)
