#!/usr/bin/env bash

source env/bin/activate
export FLASK_APP=web/index.py
python -m flask run