#!/usr/bin/env python

# Set environment to be able to import the anontunnel application
import os
import sys
sys.path.append(os.path.realpath(os.path.join(__file__, '..', '..', '..', 'anontunnel')))

from kivy.clock import Clock
from kivy.modules.recorder import Recorder

# Import python unit tests
import unittest


class TestUserInterface(unittest.TestCase):
    """
    Tests for the user interface
    """

    def setUp(self):
        """
        The set up for each test constructs a new app
        """
        import kivy
        kivy.require('1.8.0')
        from kivy.config import Config
        from kivy.interactive import InteractiveLauncher
        from kivy.base import EventLoop
        from kivy.core.window import Window
        Config.set('modules', 'recorder', '')
        from main import AnonTunnelApp
        self.ata = AnonTunnelApp()

    def stopApp(self, dt):
        """
        This should be scheduled at the end of each test to shut down the app
        """
        self.ata.stop()

    def test_settings(self):
        """
        Tests going to the settings screen
        """
        def asserts():
            self.assertEqual(self.ata.screen_manager.current, 'settings')
        self.run_recorded_test('settings.kvi', asserts)

    def test_settings_backtomain(self):
        """
        Tests going from settings screen back to the main screen
        """
        def asserts():
            self.assertEqual(self.ata.screen_manager.current, 'anontunnels')
        self.run_recorded_test('settings_backtomain.kvi', asserts)

    def test_settings_wifi_off(self):
        """
        Tests toggling the wifi setting checkbox off
        """
        def asserts():
            self.assertFalse(self.ata.screen_manager.get_screen('settings').checkbox_wifi.active)
    	self.run_recorded_test('settings_wifi_off.kvi', asserts)

    def test_settings_wifi_on(self):
        """
        Tests toggling the wifi setting checkbox on
        """
        def asserts():
            self.assertTrue(self.ata.screen_manager.get_screen('settings').checkbox_relay.active)
        self.run_recorded_test('settings_wifi_on.kvi', asserts)

    def test_settings_relay_off(self):
        """
        Tests toggling the relay setting checkbox off
        """
        def asserts():
            self.assertFalse(self.ata.screen_manager.get_screen('settings').checkbox_relay.active)
        self.run_recorded_test('settings_relay_off.kvi', asserts)

    def test_settings_relay_on(self):
        """
        Tests toggling the relay setting checkbox on
        """
        def asserts():
            self.assertTrue(self.ata.screen_manager.get_screen('settings').checkbox_relay.active)
        self.run_recorded_test('settings_relay_on.kvi', asserts)

    def test_settings_download_off(self):
        """
        Tests toggling the download setting checkbox off
        """
        def asserts():
            self.assertFalse(self.ata.screen_manager.get_screen('settings').checkbox_download.active)
        self.run_recorded_test('settings_download_off.kvi', asserts)

    def test_settings_download_on(self):
        """
        Tests toggling the download setting checkbox on
        """
        def asserts():
            self.assertTrue(self.ata.screen_manager.get_screen('settings').checkbox_download.active)
        self.run_recorded_test('settings_download_on.kvi', asserts)

    def run_recorded_test(self, kvi_file, assert_function):
        """
        Runs a recorded application test

        Keyword arguments
        kvi_file -- The recorded interaction to load
        assert_function -- A function that asserts the state at the end of the recording
        """

        def assert_app_state(dt):
            assert_function()
            Clock.schedule_once(self.stopApp, 1)

        def on_play(instance, value):
            if value is False:
                Clock.schedule_once(assert_app_state, 1)

        def perform_test(dt):
            rec = Recorder(filename=os.path.join(os.path.dirname(os.path.realpath(__file__)), kvi_file))
            rec.bind(play=on_play)
            rec.play = True

        Clock.schedule_once(perform_test, 1)
        self.ata.run()

if __name__ == "__main__":
    unittest.main()

