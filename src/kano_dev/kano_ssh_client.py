# kano_ssh_client.py
#
# Copyright (C) 2017 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# TODO: Description


from kano_settings.system.advanced import is_ssh_enabled, set_ssh_enabled

from kano_dev.utils import run_cmd

from kano_dev.paths import DROPBEAR_CONF_PATH
from kano_dev.return_codes import *


class KanoSshClient(object):

    def __init__(self):
        super(KanoSshClient, self).__init__()

    def set_enabled(self, enabled):
        """
        TODO: Description
        """
        set_ssh_enabled(enabled, with_logging=False)

    def set_root_connection(self, enabled):
        """
        TODO: Description
        """
        if enabled:
            cmd = 'sed -i \'s/DROPBEAR_EXTRA_ARGS="-g -w"/DROPBEAR_EXTRA_ARGS=""/g\' {path}'
        else:
            cmd = 'sed -i \'s/DROPBEAR_EXTRA_ARGS=""/DROPBEAR_EXTRA_ARGS="-g -w"/g\' {path}'

        cmd = cmd.format(path=DROPBEAR_CONF_PATH)
        if run_cmd(cmd):
            print "KanoSshClient: set_allow_root_connection: Failed setting" \
                " DROPBEAR_EXTRA_ARGS with cmd:\n{}".format(cmd)
            return RC_UNEXPECTED_ERROR

        return self._restart_ssh_client()

    def _restart_ssh_client(self):
        """
        TODO: Description
        """

        # TODO: Move this into kano-settings
        cmd = 'systemctl restart dropbear.service'
        if run_cmd(cmd):
            print "KanoSshClient: set_allow_root_connection: Failed restarting" \
                " dropbear with cmd:\n{}".format(cmd)
            return RC_UNEXPECTED_ERROR

    def status(self):
        """
        TODO: Description
        """
        print "SSH client enabled: {}".format(is_ssh_enabled())
        print "Root SSH allowed: {}".format(self._is_root_connection_enabled())

    def _is_root_connection_enabled(self):
        """ TODO: Description """

        with open(DROPBEAR_CONF_PATH, 'r') as dropbear_conf:
            dropbear_conf_lines = [line.strip() for line in dropbear_conf.readlines()]

        for line in dropbear_conf_lines:
            if line.startswith('DROPBEAR_EXTRA_ARGS'):
                dropbear_args = line.split('=')[1].strip('"').split()
                return ('-g' not in dropbear_args and '-w' not in dropbear_args)

        return False
