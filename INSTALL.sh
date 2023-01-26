#!/bin/sh -e

# RUN AS SU
#install usbmount (automount usb drives)
sudo sed -i "s/\(PrivateMounts *= *\).*/\1no/" /lib/systemd/system/systemd-udevd.service
apt install usbmount


#copy rc.local
cp etc/rc.local /etc/rc.local