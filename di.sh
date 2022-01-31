#!/bin/bash
rrd=$HOME"/RozetkaRul3"
if [ ! -d $rrd ]; then
  mkdir $rrd
fi
wget --ftp-user=sh --ftp-password=123123 ftp://188.168.24.94:7744/RozetkaRul3.py -O $rrd/RozetkaRul3.py
wget --ftp-user=sh --ftp-password=123123 ftp://188.168.24.94:7744/settings.json -O $rrd/settings.json
chmod +x $rrd/RozetkaRul3.py

apt-get update
apt-get install python3.8 -y
apt-get install python3-pip -y
pip3 install -U pip
pip3 install broadlink

