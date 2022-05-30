#!/bin/bash
git checkout master
git pull
source ~/env/bin/activate
python download.py --utm-url=http://localhost:8080
deactivate