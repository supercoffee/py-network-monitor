# py-network-monitor
Keep an eye on the speeds your ISP is delivering with this script.

## What it does
This script runs in the background of your mac and tests the speed of your internet. Results are logged to a sqlite database.

## Requirements
* [speedtest-cli](https://github.com/sivel/speedtest-cli)
* python3

## Installing

```
git clone https://github.com/supercoffee/py-network-monitor/
cd python-network-monitor
sudo install.sh
````

## Viewing data
Data is stored in the `speed-test-results.db` sqlite database located inside the program installation directory.
Use your favorite sqlite3 interface to view the data.

### Project Todos
* Customizable installation directory
* custom data and log directories
* uninstaller
* web GUI
