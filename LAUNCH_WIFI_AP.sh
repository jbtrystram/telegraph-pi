#! /bin/bash

sudo nmcli radio wifi off
sudo rfkill unblock wlan

sudo ifconfig wlan3 10.0.0.1/24 up
sleep 1
sudo hostapd /etc/hostapd/hostapd.conf
