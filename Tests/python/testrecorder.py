#!/usr/bin/env python
import os
os.chdir(os.path.realpath(os.path.join(__file__, '..', '..', '..', 'anontunnel')))
import sys
sys.path.append(os.path.realpath(os.path.join(__file__, '..', '..', '..')))
print sys.path
import main

import kivy
kivy.require('1.8.0')
from kivy.config import Config
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
import main

Config.set('modules', 'recorder', '')
from kivy.modules.recorder import Recorder


if __name__ == "__main__":
    Window.clearcolor = (1, 1, 1, 1)
    record = Recorder(record=True, filename='settings_wifi.kvi')
    main.AnonTunnelApp().run()
