#!/bin/bash
wget https://archive.raspberrypi.org/debian/pool/main/r/raspberrypi-firmware/raspberrypi-kernel-headers_1.20201126-1_armhf.deb
dpkg -i raspberrypi-kernel-headers_1.20201126-1_armhf.deb
rm -f raspberrypi-kernel-headers_1.20201126-1_armhf.deb

#sudo rfkill unblock wiki sudo rfkill unblock all

apt update
apt install fonts-unfonts-core -y
apt install ftp vim sox libsox-fmt-all -y
apt install python3-dev python3-pip -y
apt install libhdf5-dev libatlas-base-dev libjasper-dev libqtgui4 libqt4-test -y
apt install tesseract-ocr tesseract-ocr-kor -y
apt install curl cmake openjdk-8-jdk -y
apt install omxplayer -y
apt install libilmbase23 libopenexr-dev libswscale-dev libzbar0 -y
apt install usbmount -y
apt install python3-lxml -y

# for beautifulsoup lxml
apt install python3-bs4 -y

#apt install --reinstall raspberrypi-bootloader raspberrypi-kernel -y

# for mecab
bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)

wget https://project-downloads.drogon.net/wiringpi-latest.deb
dpkg -i wiringpi-latest.deb
rm wiringpi-latest.deb
#systemctl disable hciuart.service

pip3 install git+https://github.com/themakerrobot/x-openpibo

cd /home/pi/openpibo-os/
cp utils/boot/* /boot/
cp utils/system/rc.local /etc/
cp utils/system/startup.py /home/pi/

cd /home/pi/openpibo-os/utils/servo
./install.sh
cd /home/pi/openpibo-os/utils/mic/
./i2smic.sh