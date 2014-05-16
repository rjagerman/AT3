import os

import logging
import logging.config

import kivy
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.app import App

import sys

print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

#adjust the PYTHON_EGG_CACHE
os.environ["PYTHON_EGG_CACHE"] = "/data/data/com.devos.anontunnel1/cache"

"""
AnonTunnel CLI interface
"""

class IORedirector(object): # A general class for redirecting I/O to this Text widget.
    def __init__(self,log_textview):
        self.log_textview = log_textview

class StdoutRedirector(IORedirector): # A class for redirecting stdout to this Text widget.
    def write(self,str):
        self.log_textview.text = self.log_textview.text + str


# set the background color to white
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

class ScrollableLabel(ScrollView):
    text = StringProperty('')

class AnonTunnelScreen(BoxLayout):
    def __init__(self, **kwargs):
        self.isRunning = False
        super(AnonTunnelScreen, self).__init__(**kwargs)

        # redirect the stdout to the log_textview
        sys.stdout = StdoutRedirector(self.log_textview)

        # redirect logger to stdout
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        root.addHandler(ch)

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

class AnonTunnelApp(App):
    def build(self):
        self.ats = AnonTunnelScreen()
        return self.ats

    def on_pause(self):
        logging.warn('PAUSING -----------------------------@@@@@@@@@@@@@@@@@@@@@@----------------------')
        return True

    # we willen dat deze wordt aangeroepen zodra de app wordt gekilled
    def on_stop(self):
        logging.warn('STOPPING -----------------------------@@@@@@@@@@@@@@@@@@@@@@----------------------')
        self.ats.stopAnonTunnel()

if __name__ == '__main__':
    AnonTunnelApp().run()
