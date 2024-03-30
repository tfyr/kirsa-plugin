#!/bin/bash
cd ~/kirsa-plugin
git checkout master
git pull
source ~/env/bin/activate
date >> download.log
python download.py --utm-url=http://localhost:8080 >> download.log
deactivate