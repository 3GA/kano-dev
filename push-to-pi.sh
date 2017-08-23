#!/bin/bash

# push-to-pi.sh
#
# Sync


DEST_USER='radu'
# DEST_USER='kano'
DEST_IP='10.0.30.45'
# DEST_IP='10.0.30.230'
# DEST_IP='192.168.1.74'

DEST_DIR="$(basename `pwd`)"
DEST_STR="$(printf "%s@%s:~/%s" "$DEST_USER" "$DEST_IP" "$DEST_DIR")"


rsync -ravz -e ssh  \
    --exclude='.git' --exclude='*.pyc' --exclude='*.swp' --exclude='.DS_Store' \
    --exclude='*.o' --exclude='moc_*' --exclude='.qmake*' --exclude='__pycache__' \
    --exclude='*.app' --exclude='debug' --exclude='release' --exclude='.cache' \
    "$(pwd)/" "$USERNAME" "$DEST_STR"
