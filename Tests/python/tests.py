#!/usr/bin/env python

# Set environment to the anontunnel application
import os
os.chdir(os.path.realpath(os.path.join(__file__, '..', '..', '..', 'anontunnel')))
import sys
sys.path.append(os.path.realpath(os.path.join(__file__, '..', '..', '..')))
print sys.path
from main import AnonTunnelApp

# Set the recorder configuration
import kivy
kivy.require('1.8.0')
from kivy.config import Config
Config.set('modules', 'recorder', '')
from kivy.modules.recorder import Recorder

import unittest


class TestUserInterface(unittest.TestCase)

    def setUp(self):
        self.ata = AnonTunnelApp()

    def test_settings(self):
        self.ata.screen_manager.

    def test_settings_wifionly_on(self):
    	record = Recorder(record=True, filename='settings_wifi.kvi')

    def test_start_anontunnel(self):
        self.ata.start_anontunnel()

    def test_stop_anontunnel(self):
        pass

if __name__ == "__main__":
    unittest.main()

