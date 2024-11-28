#!/bin/bash
cd ~/kirsa-plugin
git checkout master
git pull
date >> download.log
~/env/bin/python3 download.py --utm-url=http://localhost:8080 >> download.log

