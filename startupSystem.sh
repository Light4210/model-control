#!/bin/bash

ssh-keygen -t ed25519 -C "tarnavskij2002@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
sudo apt install git -y
sudo apt install python3-pip
sudo apt-get install python3-tk
