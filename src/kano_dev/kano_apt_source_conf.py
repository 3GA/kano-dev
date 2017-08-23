# kano_apt_source_conf.py
#
# Copyright (C) 2017 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# TODO: Description


from kano_dev.utils import run_cmd

from kano_dev.paths import KANO_LIST_NAME, RASPI_LIST_NAME, KANO_SOURCES_PATH, \
    RASPI_SOURCES_PATH
from kano_dev.return_codes import *


class KanoAptSourceConf(object):
    """
    TODO: Description
    """

    KANO_SUITES = ['scratch', 'devel', 'rc', 'rc-i18n', 'release', 'release-i18n']
    KANO_REPOS = ['dev', 'prod', 'i18n']

    DEFAULT_REPO = {
        'scratch': 'dev',
        'devel': 'dev',
        'rc': 'dev',
        'rc-i18n': 'dev',
        'release': 'prod',
        'release-i18n': 'i18n'
    }

    KANO_URL = {
        'dev': 'http://dev.kano.me/archive-jessie/',
        'prod': 'http://repo.kano.me/archive-jessie/',
        'i18n': 'http://repo.kano.me/archive-jessie/'
    }
    RASPI_URL = {
        'dev': 'http://dev.kano.me/mirrors/raspberrypi-jessie/',
        'prod': 'http://repo.kano.me/raspberrypi-jessie/',
        'i18n': 'http://repo.kano.me/raspberrypi-jessie-i18n/'
    }

    def __init__(self):
        """
        TODO: Description
        """
        super(KanoAptSourceConf, self).__init__()

    def set_suite(self, suite, repo=''):
        """
        TODO: Description
        """
        if suite not in self.KANO_SUITES:
            print "Incorrect suite given! Supported ones are: {}".format(self.KANO_SUITES)
            return RC_INCORRECT_ARGS

        if repo and repo not in self.KANO_REPOS:
            print "Incorrect repo given! Supported ones are: {}".format(self.KANO_REPOS)
            return RC_INCORRECT_ARGS
        elif not repo:
            repo = self.DEFAULT_REPO[suite]

        print "Setting suite to [{}] on repo [{}]..".format(suite, repo)

        cmd = "sed -i 's# \({possible_suites}\) # {suite} #g' {path}".format(
            possible_suites='\|'.join(self.KANO_SUITES),
            suite=suite,
            path=KANO_SOURCES_PATH
        )
        if run_cmd(cmd):
            print 'KanoAptSourceConf: set_suite: Failed setting the source suite' \
                ' with cmd:\n{}'.format(cmd)
            return RC_UNEXPECTED_ERROR

        return self._set_url(repo)

    def _set_url(self, repo):
        """
        TODO: Description
        """
        cmd = "sed -i 's#http://[^ ]*.kano.me/archive-jessie/#{url}#g' {path}".format(
            url=self.KANO_URL[repo],
            path=KANO_SOURCES_PATH
        )
        if run_cmd(cmd):
            print "KanoAptSourceConf: _set_url: Failed setting the Kano sources URL" \
                " with cmd:\n{}".format(cmd)
            return RC_UNEXPECTED_ERROR

        cmd = "sed -r -i 's#http://[^ ]*.kano.me/(mirrors/|)raspberrypi-jessie(-i18n|)/#{url}#g' {path}" \
            .format(
                url=self.RASPI_URL[repo],
                path=RASPI_SOURCES_PATH
            )
        if run_cmd(cmd):
            print "KanoAptSourceConf: _set_url: Failed setting the Raspi sources URL" \
                " with cmd:\n{}".format(cmd)
            return RC_UNEXPECTED_ERROR

        return RC_SUCCESS

    def status(self):
        """
        TODO: Description
        """
        print '{}:'.format(KANO_LIST_NAME)

        with open(KANO_SOURCES_PATH, 'r') as kano_list:
            kano_list_lines = [line.strip() for line in kano_list.readlines()]

        for line in kano_list_lines:
            if line.startswith('deb'):
                print line

        print '{}:'.format(RASPI_LIST_NAME)

        with open(RASPI_SOURCES_PATH, 'r') as raspi_list:
            kano_list_lines = [line.strip() for line in raspi_list.readlines()]

        for line in kano_list_lines:
            if line.startswith('deb'):
                print line
