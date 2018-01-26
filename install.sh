#!/usr/bin/env bash

PLIST_FILE_NAME='com.bendaschel.py-network-monitor.plist'
python_path=`which python3`

install() {

    escape_path=`pwd | sed -e 's/\/'`
    cat $PLIST_FILE_NAME | \
    sed -e "s|{{ install_dir }}|$PWD|g" -e "s|{{ python_path }}|$python_path|g" -e "s|{{ env_path }}|$PATH|g" |\
    tee ~/Library/LaunchAgents/com.bendaschel.py-network-monitor.plist

    sudo launchctl unload ~/Library/LaunchAgents/com.bendaschel.py-network-monitor.plist
    sudo launchctl load ~/Library/LaunchAgents/com.bendaschel.py-network-monitor.plist
}

install