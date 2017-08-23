# test_kano_ssh_client.py
#
# Copyright (C) 2017 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# TODO: Description


import pytest
from os.path import abspath, join

from tests.fixtures.dropbear_ssh_config import ROOT_SSH, NO_ROOT_SSH
from kano_dev.paths import TEST_TEMP_DIR, DROPBEAR_CONF_NAME


class TestKanoSshClient(object):

    @pytest.mark.skipif(not pytest.is_kano_os(), reason=pytest.REASON_REQUIRES_KANO_OS)
    def test_set_root_connection_enabled(self, monkeypatch, dropbear_conf):
        """
        TODO: Description
        """
        from kano_dev import kano_ssh_client as k

        # Create the expected config line from the parameters used by the fixture.
        expected_dropbear_extra_args = 'DROPBEAR_EXTRA_ARGS="{}"'.format(
            ROOT_SSH['DROPBEAR_EXTRA_ARGS']
        )

        # Mock the paths to the dropbear configuration file. This tricks the function
        # call to do the work at a different path.
        monkeypatch.setattr(
            k, 'DROPBEAR_CONF_PATH', abspath(join(TEST_TEMP_DIR, DROPBEAR_CONF_NAME))
        )

        # Call the function to be tested.
        k.KanoSshClient().set_root_connection(True)

        # Read back the dropbear configuration file.
        with open(dropbear_conf.name, 'r') as dropbear_conf:
            dropbear_conf_lines = [line.strip() for line in dropbear_conf.readlines()]

        assert(expected_dropbear_extra_args in dropbear_conf_lines)

    @pytest.mark.skipif(not pytest.is_kano_os(), reason=pytest.REASON_REQUIRES_KANO_OS)
    def test_set_root_connection_disabled(self, monkeypatch, dropbear_conf):
        """
        TODO: Description
        """
        from kano_dev import kano_ssh_client as k

        # Create the expected config line from the parameters used by the fixture.
        expected_dropbear_extra_args = 'DROPBEAR_EXTRA_ARGS="{}"'.format(
            NO_ROOT_SSH['DROPBEAR_EXTRA_ARGS']
        )

        # Mock the paths to the dropbear configuration file. This tricks the function
        # call to do the work at a different path.
        monkeypatch.setattr(
            k, 'DROPBEAR_CONF_PATH', abspath(join(TEST_TEMP_DIR, DROPBEAR_CONF_NAME))
        )

        # Call the function to be tested.
        k.KanoSshClient().set_root_connection(False)

        # Read back the dropbear configuration file.
        with open(dropbear_conf.name, 'r') as dropbear_conf:
            dropbear_conf_lines = [line.strip() for line in dropbear_conf.readlines()]

        assert(expected_dropbear_extra_args in dropbear_conf_lines)

    @pytest.mark.skipif(
        not pytest.is_pypkg_installed(['kano_settings']),
        reason=pytest.REASON_MISSING_PYPKG
    )
    def test_is_root_connection_enabled(self, monkeypatch, dropbear_conf):
        """
        TODO: Description
        """
        from kano_dev import kano_ssh_client as k

        # Read back the dropbear configuration file.
        with open(dropbear_conf.name, 'r') as dropbear_conf:
            dropbear_conf_lines = [line.strip() for line in dropbear_conf.readlines()]

        root_ssh_line = 'DROPBEAR_EXTRA_ARGS="{}"'.format(ROOT_SSH['DROPBEAR_EXTRA_ARGS'])
        no_root_ssh_line = 'DROPBEAR_EXTRA_ARGS="{}"'.format(NO_ROOT_SSH['DROPBEAR_EXTRA_ARGS'])

        # Determine what the function should return from what is in the configuration.
        if root_ssh_line in dropbear_conf_lines:
            expected_rv = True
        elif no_root_ssh_line in dropbear_conf_lines:
            expected_rv = False

        # Mock the paths to the dropbear configuration file. This tricks the function
        # call to do the work at a different path.
        monkeypatch.setattr(
            k, 'DROPBEAR_CONF_PATH', abspath(join(TEST_TEMP_DIR, DROPBEAR_CONF_NAME))
        )

        # Calling the function to be tested.
        rv = k.KanoSshClient()._is_root_connection_enabled()

        assert(expected_rv == rv)
