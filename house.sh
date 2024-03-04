#!/bin/sh

cd /home/dim/model-control
xinput map-to-output 10 HDMI-1
sleep 6
sudo chmod 777 /dev/ttyUSB0
sleep 1
python3 /home/dim/model-control/app.py
