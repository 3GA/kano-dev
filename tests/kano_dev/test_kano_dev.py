# test_kano_dev.py
#
# Copyright (C) 2017 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# TODO: Description


import os
import imp
import pytest

from kano_dev.paths import LOCAL_PATH, KANO_DEV_NAME, KANO_DEV_PATH


class TestKanoDev(object):

    @pytest.mark.skipif(
        not pytest.is_pypkg_installed(['docopt', 'kano_settings']),
        reason=pytest.REASON_MISSING_PYPKG
    )
    def test_cmdline_interface(self, monkeypatch):
        """
        # TODO: Description
        """
        import docopt

        kano_dev = imp.load_source(KANO_DEV_NAME, os.path.join(LOCAL_PATH, KANO_DEV_PATH))

        monkeypatch.setattr(kano_dev.sys, 'argv', [KANO_DEV_NAME, 'production'])
        args = docopt.docopt(kano_dev.__doc__)

        print args

        # assert 'production' in args
        assert False
