# app_args.py
#
# Copyright (C) 2017 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# TODO: Description


import pytest

from kano_dev.kano_apt_source_conf import KanoAptSourceConf
from kano_dev.kano_world_api_conf import KanoWorldApiConf


# TODO: description
EXPECTED_SUITE_ARGS = KanoAptSourceConf.KANO_SUITES
ALL_SUITE_ARGS = EXPECTED_SUITE_ARGS + [42, 'releasy-mc-release-face']

# TODO: description
EXPECTED_REPO_ARGS = KanoAptSourceConf.KANO_REPOS + ['']
ALL_REPO_ARGS = EXPECTED_REPO_ARGS + [0.07, 'that-repo-one']

# TODO: description
EXPECTED_API_ARGS = KanoWorldApiConf.API_MODES
ALL_API_ARGS = EXPECTED_API_ARGS + ['scratchy', 'was-it-prod', 12345678]


@pytest.fixture(scope='function', params=(EXPECTED_SUITE_ARGS))
def expected_suite_arg(request):
    """
    # TODO: Description
    """
    return request.param


@pytest.fixture(scope='function', params=(ALL_SUITE_ARGS))
def all_suite_arg(request):
    """
    # TODO: Description
    """
    return request.param


@pytest.fixture(scope='function', params=(EXPECTED_REPO_ARGS))
def expected_repo_arg(request):
    """
    # TODO: Description
    """
    return request.param


@pytest.fixture(scope='function', params=(ALL_REPO_ARGS))
def all_repo_arg(request):
    """
    # TODO: Description
    """
    return request.param


@pytest.fixture(scope='function', params=(EXPECTED_API_ARGS))
def expected_api_arg(request):
    """
    # TODO: Description
    """
    return request.param


@pytest.fixture(scope='function', params=(ALL_API_ARGS))
def all_api_arg(request):
    """
    # TODO: Description
    """
    return request.param
