import os
import logging

import kivy
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.app import App
from kivy.lib import osc

import sys


#adjust the PYTHON_EGG_CACHE
# os.environ["PYTHON_EGG_CACHE"] = "/data/data/com.devos.anontunnel1/cache"
os.environ["PYTHON_EGG_CACHE"] = "/data/data/com.AT3.anontunnel/cache"

"""
AnonTunnel CLI interface
"""

# set the background color to white
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

class ScrollableLabel(ScrollView):
    text = StringProperty('')

class AnonTunnelScreen(BoxLayout):
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
            service = AndroidService('Anonymous downloading', 'Anonymous tunnels are running...')
            service.start('Anonymous tunnels service started')
            self.service = service

        else:
            print 'Stopping the anonymous tunnels...'
            self.tunnel_togglebutton.text = 'Off'
            self.isRunning = False
            self.service.stop()

class AnonTunnelApp(App):
    def build(self):
        osc.init()
        oscid = osc.listen(port=3002)
        osc.bind(oscid, self.receivedLog, '/log')
        self.ats = AnonTunnelScreen()
        return self.ats

    def receivedLog(self, message, *args):
        self.ats.log_textview.text += '%s' % message[2]

    def on_pause(self):
        return True

    # we willen dat deze wordt aangeroepen zodra de app wordt gekilled
    def on_stop(self):
        self.ats.stopAnonTunnel()

if __name__ == '__main__':
    AnonTunnelApp().run()
