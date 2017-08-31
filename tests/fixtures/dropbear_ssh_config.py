# dropbear_ssh_config.py
#
# Copyright (C) 2017 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# TODO: Description


import os
import pytest
import textwrap

from kano_dev.paths import TEST_TEMP_DIR, DROPBEAR_CONF_NAME


DROPBEAR_CONF = textwrap.dedent("""
    # the TCP port that Dropbear listens on
    DROPBEAR_PORT=22

    # any additional arguments for Dropbear
    DROPBEAR_EXTRA_ARGS="{DROPBEAR_EXTRA_ARGS}"

    # specify an optional banner file containing a message to be
    # sent to clients before they connect, such as "/etc/issue.net"
    DROPBEAR_BANNER=""

    # RSA hostkey file (default: /etc/dropbear/dropbear_rsa_host_key)
    #DROPBEAR_RSAKEY="/etc/dropbear/dropbear_rsa_host_key"

    # DSS hostkey file (default: /etc/dropbear/dropbear_dss_host_key)
    #DROPBEAR_DSSKEY="/etc/dropbear/dropbear_dss_host_key"

    # Receive window size - this is a tradeoff between memory and
    # network performance
    DROPBEAR_RECEIVE_WINDOW=65536
    """)

NO_ROOT_SSH = {
    'DROPBEAR_EXTRA_ARGS': '-g -w',
}

ROOT_SSH = {
    'DROPBEAR_EXTRA_ARGS': '',
}


@pytest.fixture(scope='function', params=[NO_ROOT_SSH, ROOT_SSH])
def dropbear_conf(real_temp_dir, request):
    """
    # TODO: Description
    """
    dropbear_conf_path = os.path.abspath(os.path.join(TEST_TEMP_DIR, DROPBEAR_CONF_NAME))

    config = DROPBEAR_CONF.format(
        DROPBEAR_EXTRA_ARGS=request.param['DROPBEAR_EXTRA_ARGS']
    )

    with open(dropbear_conf_path, 'w') as dropbear_conf:
        dropbear_conf.write(config)

    yield {
        'file': dropbear_conf,
        'param': request.param
    }

    # Clean up code, remove the file altogether.
    if os.path.exists(dropbear_conf_path):
        os.remove(dropbear_conf_path)
