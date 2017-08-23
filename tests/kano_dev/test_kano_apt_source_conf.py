# test_kano_apt_source_conf.py
#
# Copyright (C) 2017 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# TODO: Description


import pytest
import platform
from os.path import abspath, join

from kano_dev import kano_apt_source_conf as k

from kano_dev.paths import TEST_TEMP_DIR, KANO_LIST_NAME, RASPI_LIST_NAME
from kano_dev.return_codes import *


class TestKanoAptSourceConf(object):

    def test_default_repo_constant(self):
        """
        # TODO: Description
        """
        kano_suites_set = set(k.KanoAptSourceConf.KANO_SUITES)
        kano_repos_set = set(k.KanoAptSourceConf.KANO_REPOS)
        default_repo_keys_set = set(k.KanoAptSourceConf.DEFAULT_REPO.iterkeys())
        default_repo_values_set = set(k.KanoAptSourceConf.DEFAULT_REPO.itervalues())

        assert(
            default_repo_keys_set == kano_suites_set and
            default_repo_values_set <= kano_repos_set
        )

    def test_url_constants(self):
        """
        # TODO: Description
        """
        kano_repos_set = set(k.KanoAptSourceConf.KANO_REPOS)
        kano_url_keys_set = set(k.KanoAptSourceConf.KANO_URL.iterkeys())
        raspi_url_keys_set = set(k.KanoAptSourceConf.RASPI_URL.iterkeys())

        assert(
            kano_url_keys_set == kano_repos_set and
            raspi_url_keys_set == kano_repos_set
        )

    def test_set_suite_arg_checking(self, all_suite_arg, all_repo_arg):
        """
        # TODO: Description
        """
        rc = k.KanoAptSourceConf().set_suite(all_suite_arg, repo=all_repo_arg)

        if all_suite_arg in k.KanoAptSourceConf.KANO_SUITES and \
           (not all_repo_arg or all_repo_arg in k.KanoAptSourceConf.KANO_REPOS):
            assert rc != RC_INCORRECT_ARGS
        else:
            assert rc == RC_INCORRECT_ARGS

    @pytest.mark.skipif(platform.system() != 'Linux', reason=pytest.REASON_USES_SED)
    def test_set_suite_valid_lists(self, monkeypatch, kano_list, raspi_list, expected_suite_arg, expected_repo_arg):
        """
        # TODO: Description
        """

        # Set the <repo> optional argument to the default value.
        if not expected_repo_arg:
            expected_repo_arg = k.KanoAptSourceConf.DEFAULT_REPO[expected_suite_arg]

        # Set the expected output values.
        expected_kano_packages_source = 'deb {url} {suite} main'.format(
            url=k.KanoAptSourceConf.KANO_URL[expected_repo_arg],
            suite=expected_suite_arg
        )
        expected_urgent_source = 'deb {url} release-urgent main'.format(
            url=k.KanoAptSourceConf.KANO_URL[expected_repo_arg]
        )
        expected_raspi_packages_source = 'deb {url} jessie main ui'.format(
            url=k.KanoAptSourceConf.RASPI_URL[expected_repo_arg]
        )

        # Mock the paths to the kano and raspi list files. This tricks the function
        # call to do the work at a different path.
        monkeypatch.setattr(
            k, 'KANO_SOURCES_PATH', abspath(join(TEST_TEMP_DIR, KANO_LIST_NAME))
        )
        monkeypatch.setattr(
            k, 'RASPI_SOURCES_PATH', abspath(join(TEST_TEMP_DIR, RASPI_LIST_NAME))
        )

        # Call the function to be tested.
        k.KanoAptSourceConf().set_suite(expected_suite_arg, repo=expected_repo_arg)

        # Read back the kano and raspi list files.
        with open(kano_list.name, 'r') as kano_list:
            kano_list_lines = [line.strip() for line in kano_list.readlines()]

        with open(raspi_list.name, 'r') as raspi_list:
            raspi_list_lines = [line.strip() for line in raspi_list.readlines()]

        assert(
            expected_kano_packages_source in kano_list_lines and
            expected_urgent_source in kano_list_lines and
            expected_raspi_packages_source in raspi_list_lines
        )
