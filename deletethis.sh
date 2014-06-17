./distribute.sh -m "openssl kivy m2crypto pycrypto twisted sqlite3 pyasn1 tribler netifaces libtorrent apsw" -d AT3
 
Build:
./build.py --package org.tribler.at3.anontunnel --name anontunnel1 --version 1.0 --dir /home/laurens/Desktop/AT3/anontunnel debug --permission INTERNET --icon '/home/laurens/Desktop/AT3/anontunnel/images/tribler_applogo.png' --presplash '/home/laurens/Desktop/AT3/anontunnel/images/splash.jpg'
