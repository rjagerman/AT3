[![Build Status](http://jenkins.tribler.org/job/Build-AT3-ARM-32/badge/icon)](http://jenkins.tribler.org/job/Build-AT3-ARM-32/)

![Android Tor Tribler Tunnelling (AT3)](http://forum.tribler.org/download/file.php?id=203)

Android Tor Tribler Tunneling (AT3) is a sub project from the Tribler project from the Parallel and Distributed Systems group from the Technical University of Delft. This project is based on the [Python for Android framework](https://github.com/kivy/python-for-android/). The code this app runs can be found at the [main Tribler project](https://github.com/Tribler/tribler), more specifically from [Pull Request #581](https://github.com/Tribler/tribler/pull/581).

![Test download succeeded!](http://forum.tribler.org/download/file.php?id=204)

Goal
====

Our goal it to create an Android application that enables anonymous downloading using peer-to-peer torrenting with help of the so called Tor-tunnels that make use of the Tor protocol. This project works close with the [TSAP sub project](https://github.com/wtud/tsap), which are currently building a fancy GUI and enable torrent downloading through their interface.
The final goal is to combine these two projects to create a decentralized, anonymous peer-to-peer streaming app where content can be featured on.

Building the app from source
============================

To build this app, one needs to execute the following steps:

1. Clone the Python for Android framework and remember the location where it is saved.
2. Next you can clone this project on a place where you prefer it, we will assume you've named the folder AT3.
3. Go to the AT3 folder
4. Adapt the build.config file to include your icon (optional), splashimage (optional) and path the python for android (required).
5. Call the ``build.sh`` script.
6. If all goes well, the app should be created in the AT3/app folder.
7. To install, make sure your device is connected to your computer and call ``adb install <.apk file>``
 
