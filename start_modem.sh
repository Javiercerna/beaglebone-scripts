/usr/sbin/usb_modeswitch -c /etc/usb_modeswitch.d/12d1:15d4
sleep 5
wvdial &
sleep 5
sudo python /home/debian/remote-drone/mavlink/dronekit_client.py &
