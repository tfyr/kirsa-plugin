#!/bin/bash
cd ~/kirsa-plugin
git checkout master
git pull
date >> download.log
#~/env/bin/python3 download.py --utm-url=http://localhost:8088 >> download.log
~/kirsa-plugin/venv/venv_python/bin/python download.py --utm-url=http://localhost:8088 >> download.log
#--backend-url=http://localhost:8015/file/
