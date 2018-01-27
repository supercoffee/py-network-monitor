# py-network-monitor
Keep an eye on the speeds your ISP is delivering with this script.

## What it does
This script runs in the background of your mac and tests the speed of your internet. Results are logged to a sqlite database.

## Requirements
* [speedtest-cli](https://github.com/sivel/speedtest-cli)
* python3
* Flask (for web UI)

## Installing

```
git clone https://github.com/supercoffee/py-network-monitor/
cd python-network-monitor
sudo install.sh
````

## Viewing data
* start the webserver from this project directory `./server.sh`
* Open a browser and navigate to `localhost:5000`

### Project Todos
* Customizable installation directory
* custom data and log directories
    * load data from config file
* uninstaller
* Linux support
* Run webserver as a daemon
* consolidate dependencies into a python virtual env
