import os
try:
    import android
    os.environ["PYTHON_EGG_CACHE"] = "/data/data/org.tribler.at3.anontunnel/cache"
    os.environ['TRIBLER_STATE_DIR'] = "/sdcard/org.tribler.at3.anontunnel/.tribler"
except ImportError:
    os.environ['TRIBLER_STATE_DIR'] = "./.tribler"
    import Tribler
import logging
import sys
import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from screens import AnonTunnelScreen, SettingsScreen


class AnonTunnelApp(App):
    """
    The main app
    """

    screen_manager = None

    def build(self):
        """
        Construct the screen manager with the appropriate screens
        """
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(AnonTunnelScreen(name='anontunnels'))
        self.screen_manager.add_widget(SettingsScreen(name='settings'))

        return self.screen_manager

    def received_log(self, message, *args):
        """
        When receiving log messages write them to the text view
        """
        self.ats.log_textview.text += '%s' % message[2]

    def on_pause(self):
        """
        Do nothing when the app is paused
        """
        return True
    
    def on_stop(self):
        """
        Do nothing when the application is stopped
        """
        return True

if __name__ == '__main__':
    Window.clearcolor = (1, 1, 1, 1)
    AnonTunnelApp().run()
