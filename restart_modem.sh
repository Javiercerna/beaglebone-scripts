#!/usr/bin/env bash

echo "New connection attempt" >> /home/debian/scripts/connection_log.txt
echo $(date +'%d/%m/%Y %r') >> /home/debian/scripts/connection_log.txt

sleep 10
/usr/sbin/usb_modeswitch -c /etc/usb_modeswitch.d/12d1:15d4
sleep 5

while !(ping -q -c 1 -W 1 8.8.8.8 >/dev/null); do
  echo "IPv4 is down. Running wvdial..." >> /home/debian/scripts/connection_log.txt
  wvdial > /home/debian/scripts/connection_log.txt 2>&1 &
  sleep 15
done
echo "IPv4 is up" >> /home/debian/scripts/connection_log.txt

