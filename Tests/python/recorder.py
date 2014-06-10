#!/usr/bin/env python
import os
import sys
sys.path.append(os.path.realpath(os.path.join(__file__, '..', '..', '..', 'anontunnel')))
import main

import kivy
kivy.require('1.8.0')
from kivy.config import Config
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
Config.set('modules', 'recorder', '')
from kivy.modules.recorder import Recorder
import main


if __name__ == "__main__":
    Window.clearcolor = (1, 1, 1, 1)
    print 'Please enter the name of the recording and press ENTER to start'
    fname = raw_input('Name of the recording: ')
    rec = Recorder(filename=os.path.join('Tests', 'python', '%s.kvi' % fname))
    rec.record = True
    main.AnonTunnelApp().run()
