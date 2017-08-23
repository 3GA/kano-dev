# kano_world_api_conf.py
#
# Copyright (C) 2017 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# TODO: Description


import os
import textwrap

from kano_dev.utils import writefile, rmfile

from kano_dev.paths import KANO_WORLD_CONF_NAME, KANO_CONTENT_CONF_NAME, \
    KANO_WORLD_CONF_PATH, KANO_CONTENT_CONF_PATH
from kano_dev.return_codes import *


class KanoWorldApiConf(object):
    """
    TODO: Description
    """

    API_MODES = ['staging', 'prod', 'prod-i18n']

    KANO_WORLD = {
        'staging': textwrap.dedent("""
            api_url: https://api-staging.kano.me
            world_url: http://world-staging.kano.me
            """),
        'prod': None,
        'prod-i18n': None
    }
    KANO_CONTENT = {
        'staging': 'api-url: http://kano-content-api-test.herokuapp.com',
        'prod': None,
        'prod-i18n': 'api-url: http://content-api-i18n.kano.me'
    }

    def __init__(self):
        super(KanoWorldApiConf, self).__init__()

    def set_api(self, api_mode):
        """
        TODO: Description
        """
        if api_mode not in self.API_MODES:
            print "Incorrect API mode given! Supported ones are: {}".format(self.API_MODES)
            return RC_INCORRECT_ARGS

        print "Setting Kano World API to [{}]..".format(api_mode)

        self._set_api_helper(KANO_WORLD_CONF_PATH, self.KANO_WORLD[api_mode])
        self._set_api_helper(KANO_CONTENT_CONF_PATH, self.KANO_CONTENT[api_mode])

    def _set_api_helper(self, conf_path, config):
        """ TODO: Description """

        if config:
            writefile(conf_path, config)
        else:
            rmfile(conf_path)

    def status(self):
        """
        TODO: Description
        """
        self._status_helper(KANO_WORLD_CONF_NAME, KANO_WORLD_CONF_PATH)
        self._status_helper(KANO_CONTENT_CONF_NAME, KANO_CONTENT_CONF_PATH)

    def _status_helper(self, file_name, file_path):
        """ TODO: Description """

        print '{}:'.format(file_name)

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                print file.read().strip()
        else:
            print "File not found (Production setup)."
