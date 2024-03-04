#!/bin/sh

cd /home/dim/model-control
xinput map-to-output 20 HDMI-1
sleep 7
python3 /home/dim/model-control/app.py
