# test_kano_world_api_conf.py
#
# Copyright (C) 2017 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# TODO: Description


import os

from kano_dev import kano_world_api_conf as k

from kano_dev.paths import KANO_WORLD_CONF_PATH, KANO_CONTENT_CONF_PATH
from kano_dev.return_codes import *


class TestKanoWorldApiConf(object):

    def test_kano_constants(self):
        """
        # TODO: Description
        """
        api_modes_set = set(k.KanoWorldApiConf.API_MODES)
        kano_world_keys_set = set(k.KanoWorldApiConf.KANO_WORLD)
        kano_content_keys_set = set(k.KanoWorldApiConf.KANO_CONTENT)

        assert(
            kano_world_keys_set == api_modes_set and
            kano_content_keys_set == api_modes_set
        )

    def test_set_api_arg_checking(self, fs, all_api_arg):
        """
        # TODO: Description
        """

        # Faking the two config files the function will run on.
        fs.CreateFile(KANO_WORLD_CONF_PATH)
        fs.CreateFile(KANO_CONTENT_CONF_PATH)

        rc = k.KanoWorldApiConf().set_api(all_api_arg)

        if all_api_arg in k.KanoWorldApiConf.API_MODES:
            assert rc != RC_INCORRECT_ARGS
        else:
            assert rc == RC_INCORRECT_ARGS

    def test_set_api_valid_kano_world(self, fs, expected_api_arg):
        """
        # TODO: Description
        """
        config = k.KanoWorldApiConf.KANO_WORLD[expected_api_arg]
        if not config:
            return True

        # TODO: Test the function with and without a file already there.
        if os.path.exists(KANO_WORLD_CONF_PATH):
            fs.RemoveFile(KANO_WORLD_CONF_PATH)

        # Fake the other config the function needs, but we don't test here.
        fs.CreateFile(KANO_CONTENT_CONF_PATH)

        # Call the function to be tested.
        k.KanoWorldApiConf().set_api(expected_api_arg)

        # Read back the modified file and create sets of lines in the files.
        with open(KANO_WORLD_CONF_PATH, 'r') as fake_file:
            lines_set = set([line.strip() for line in fake_file.readlines()])

        expected_lines_set = set([line.strip() for line in config.split('\n')])

        assert(
            lines_set == expected_lines_set
        )

    def test_set_api_kano_world_removed(self, fs, expected_api_arg):
        """
        # TODO: Description
        """
        if k.KanoWorldApiConf.KANO_WORLD[expected_api_arg]:
            return True

        fs.CreateFile(KANO_WORLD_CONF_PATH)

        # Fake the other config the function needs, but we don't test here.
        fs.CreateFile(KANO_CONTENT_CONF_PATH)

        # Call the function to be tested.
        k.KanoWorldApiConf().set_api(expected_api_arg)

        assert(
            not os.path.exists(KANO_WORLD_CONF_PATH)
        )

    def test_set_api_valid_kano_content(self, fs, expected_api_arg):
        """
        # TODO: Description
        """
        config = k.KanoWorldApiConf.KANO_CONTENT[expected_api_arg]
        if not config:
            return True

        # TODO: Test the function with and without a file already there.
        if os.path.exists(KANO_CONTENT_CONF_PATH):
            fs.RemoveFile(KANO_CONTENT_CONF_PATH)

        # Fake the other config the function needs, but we don't test here.
        fs.CreateFile(KANO_WORLD_CONF_PATH)

        # Call the function to be tested.
        k.KanoWorldApiConf().set_api(expected_api_arg)

        # Read back the modified file and create sets of lines in the files.
        with open(KANO_CONTENT_CONF_PATH, 'r') as fake_file:
            lines_set = set([line.strip() for line in fake_file.readlines()])

        expected_lines_set = set([line.strip() for line in config.split('\n')])

        assert(
            lines_set == expected_lines_set
        )

    def test_set_api_kano_content_removed(self, fs, expected_api_arg):
        """
        # TODO: Description
        """
        if k.KanoWorldApiConf.KANO_CONTENT[expected_api_arg]:
            return True

        fs.CreateFile(KANO_CONTENT_CONF_PATH)

        # Fake the other config the function needs, but we don't test here.
        fs.CreateFile(KANO_WORLD_CONF_PATH)

        # Call the function to be tested.
        k.KanoWorldApiConf().set_api(expected_api_arg)

        assert(
            not os.path.exists(KANO_CONTENT_CONF_PATH)
        )
