import os
<<<<<<< HEAD
#adjust the PYTHON_EGG_CACHE
os.environ["PYTHON_EGG_CACHE"] = "/data/data/org.tribler.at3.anontunnel/cache"

#adjust the TRIBLER_STATE_DIR
=======
os.environ["PYTHON_EGG_CACHE"] = "/data/data/org.tribler.at3.anontunnel/cache"
>>>>>>> 23905f27ab1be3eacdd21086d1db900fe5bd1e7c
os.environ['TRIBLER_STATE_DIR'] = "/sdcard/org.tribler.at3.anontunnel/.tribler"

import logging

import kivy
kivy.require('1.8.0')
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.app import App
from kivy.lib import osc
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout

import sys

"""
AnonTunnel CLI interface
"""

# set the background color to white
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

class ScrollableLabel(ScrollView):
    text = StringProperty('')

class AnonTunnelScreen(Screen):
    def __init__(self, **kwargs):
        self.isRunning = False
        super(AnonTunnelScreen, self).__init__(**kwargs)

    def stopAnonTunnel(self):
        if self.isRunning:
            self.isRunning = False
            self.service.stop()

    def toggleAnonTunnel(self):
        if not self.isRunning:
            self.tunnel_togglebutton.text = 'On'
            self.isRunning = True
            print 'Sending start request'
            from android import AndroidService
            service = AndroidService('Anonymous downloading Service', 'Anonymous tunnels are running...')
            service.start('Anonymous tunnels service started')
            self.service = service

        else:
            print 'Stopping the anonymous tunnels...'
            self.tunnel_togglebutton.text = 'Off'
            self.isRunning = False
            self.service.stop()

# Set the SettingScreen
class SettingsScreen(Screen):
    pass

class AnonTunnelApp(App):

    sm = None

    def build(self):
        osc.init()
        oscid = osc.listen(port=3002)
        osc.bind(oscid, self.receivedLog, '/log')
        
        self.sm = ScreenManager()
        self.sm.add_widget(AnonTunnelScreen(name='anontunnels'))
        self.sm.add_widget(SettingsScreen(name='settings'))

        return self.sm

    def receivedLog(self, message, *args):
        self.ats.log_textview.text += '%s' % message[2]

    def on_pause(self):
        logging.warn('PAUSING -----------------------------@@@@@@@@@@@@@@@@@@@@@@----------------------')
        return True

    # we willen dat deze wordt aangeroepen zodra de app wordt gekilled
    def on_stop(self):
        logging.warn('STOPPING -----------------------------@@@@@@@@@@@@@@@@@@@@@@----------------------')
        self.ats.stopAnonTunnel()

if __name__ == '__main__':
    AnonTunnelApp().run()
