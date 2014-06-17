import os
try:
    import android
    os.environ["PYTHON_EGG_CACHE"] = "/data/data/org.tribler.at3.anontunnel/cache"
    os.environ['TRIBLER_STATE_DIR'] = "/sdcard/org.tribler.at3.anontunnel/.tribler"
except ImportError:
    os.environ['TRIBLER_STATE_DIR'] = "./.tribler"
import logging
import sys
import kivy
import psutil
kivy.require('1.8.0')
from collections import deque
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.lib import osc
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.resources import resource_add_path, resource_remove_path
from screens import AnonTunnelScreen, SettingsScreen


class AnonTunnelApp(App):
    """
    The main app
    """

    screen_manager = None
    max_lines = 128

    def load_kv(self, filename=''):
        """
        Loads a kivy language file manually
        """
        resource_add_path(os.path.dirname(os.path.abspath(__file__)))
        Builder.load_file(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'anontunnel.kv'))

    def build(self):
        """
        Construct the screen manager with the appropriate screens
        """
        Window.clearcolor = (1, 1, 1, 1)
        
        self.lines = deque([])
        self.screens = {'anontunnels': AnonTunnelScreen(name='anontunnels'),
                        'settings': SettingsScreen(name='settings')}
        self.screen_manager = ScreenManager()
        for screen in self.screens.values():
            self.screen_manager.add_widget(screen)
        
        osc.init()
        self.oscid = osc.listen(ipAddr='127.0.0.1', port=9000)
        osc.bind(self.oscid, self.received_status, '/status')
        Clock.schedule_interval(lambda *x: osc.readQueue(), 0)

        return self.screen_manager

    def received_status(self, status, *args):
        """
        When receiving status updates, update the correct labels
        """
        self.screens['anontunnels'].circuits.text = '%d' % status[2]
        self.screens['anontunnels'].relays.text = '%d' % status[3]
        self.screens['anontunnels'].enter_speed.text = '%.2f KB/s' % status[4]
        self.screens['anontunnels'].relay_speed.text = '%.2f KB/s' % status[5]
        self.screens['anontunnels'].exit_speed.text = '%.2f KB/s' % status[6]
        self.screens['anontunnels'].download_speed.text = '%.2f KB/s' % status[7]
        self.screens['anontunnels'].download_progress.text = '%.2f %%' % status[8]
        self.screens['anontunnels'].cpu.text = '%s' % status[9]

    def on_pause(self):
        """
        Do nothing when the app is paused
        """
        return True
    
    def on_stop(self):
        """
        Unload the kivy language file when the application stops
        """
        Builder.unload_file(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'anontunnel.kv'))
        resource_remove_path(os.path.dirname(os.path.abspath(__file__)))
        osc.dontListen(self.oscid)
        return True

if __name__ == '__main__':
    AnonTunnelApp().run()
