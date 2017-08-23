# utils.py
#
# Copyright (C) 2017 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# Helper and utility functions.


import os
import signal
import subprocess


def restore_signals():
    signals = ('SIGPIPE', 'SIGXFZ', 'SIGXFSZ')
    for sig in signals:
        if hasattr(signal, sig):
            signal.signal(getattr(signal, sig), signal.SIG_DFL)


def run_cmd(cmd):
    """
    TODO: Description
    """
    env = os.environ.copy()

    process = subprocess.Popen(
        cmd,
        shell=True,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        preexec_fn=restore_signals
    )

    stdout, stderr = process.communicate()
    returncode = process.returncode
    return returncode


def rmfile(path):
    """
    TODO: Description
    """
    if os.path.exists(path):
        os.remove(path)


def writefile(path, contents):
    """
    TODO: Description
    """
    with open(path, 'w') as file:
        file.write(contents)


def is_root():
    """
    TODO: Description
    """
    return (os.geteuid() == 0)
