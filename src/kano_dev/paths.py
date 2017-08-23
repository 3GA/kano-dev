# paths.py
#
# Copyright (C) 2017 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# All the necessary paths used in this project.


from os.path import abspath, dirname, join


LOCAL_PATH = abspath(join(dirname(__file__), '..', '..'))

BINARIES_DIR = 'bin'
RESOURCES_DIR = 'res'
SOURCES_DIR = 'src'
TESTS_DIR = 'tests'
TEST_TEMP_DIR = '.temp'

KANO_DEV_NAME = 'kano-dev'
KANO_DEV_PATH = join(BINARIES_DIR, KANO_DEV_NAME)

KANO_LIST_NAME = 'kano.list'
RASPI_LIST_NAME = 'raspi.list'
APT_SOURCES_PATH = '/etc/apt/sources.list.d'
KANO_SOURCES_PATH = join(APT_SOURCES_PATH, KANO_LIST_NAME)
RASPI_SOURCES_PATH = join(APT_SOURCES_PATH, RASPI_LIST_NAME)

KANO_WORLD_CONF_NAME = 'kano-world.conf'
KANO_CONTENT_CONF_NAME = 'kano-content.conf'
KANO_WORLD_CONF_BASE_PATH = '/etc'
KANO_WORLD_CONF_PATH = join(KANO_WORLD_CONF_BASE_PATH, KANO_WORLD_CONF_NAME)
KANO_CONTENT_CONF_PATH = join(KANO_WORLD_CONF_BASE_PATH, KANO_CONTENT_CONF_NAME)

DROPBEAR_CONF_NAME = 'dropbear'
DROPBEAR_CONF_BASE_PATH = '/etc/default'
DROPBEAR_CONF_PATH = join(DROPBEAR_CONF_BASE_PATH, DROPBEAR_CONF_NAME)
