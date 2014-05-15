import logging
import logging.config
import os

import kivy
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.app import App

#adjust the PYTHON_EGG_CACHE
os.environ["PYTHON_EGG_CACHE"] = "/data/data/com.AT3.anontunnel/cache"

"""
AnonTunnel CLI interface
"""

print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
print os.getcwd()
print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'


# set the background color to white
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

class IORedirector(object): # A general class for redirecting I/O to this Text widget.
    def __init__(self,log_textview):
        self.log_textview = log_textview

class StdoutRedirector(IORedirector): # A class for redirecting stdout to this Text widget.
    def write(self,str):
        self.log_textview.text = self.log_textview.text+ str

class StderrRedirector(IORedirector): # A class for redirecting stderr to this Text widget.
    def write(self,str):
        self.log_textview.text = self.log_textview.text+ str

class AnonTunnelScreen(BoxLayout):
    def __init__(self, **kwargs):
        self.isRunning = False
        super(AnonTunnelScreen, self).__init__(**kwargs)

        # redirect the stdout to the log_textview
        sys.stdout = StdoutRedirector(self.log_textview)
        sys.stderr = StderrRedirector(self.log_textview)

        # redirect logger to stdout
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        ch = logging.StreamHandler(sys.stderr)
        ch.setLevel(logging.DEBUG)
        root.addHandler(ch)

    def toggleAnonTunnel(self):
        if not self.isRunning:
            self.isRunning = True
            print 'Sending start request'
            from android import AndroidService
            service = AndroidService('Anonymous downloading Service', 'Anonymous tunnels are running...')
            service.start('Anonymous tunnels service started')
            self.service = service
        else:
            print 'Stopping the anonymous tunnels...'
            self.isRunning = False
            self.service.stop()

class AnonTunnelApp(App):
    def build(self):
        self.ats = AnonTunnelScreen()
        return self.ats

    def on_destroy(self):
        self.ats.stopAnonTunnel()

if __name__ == '__main__':
    AnonTunnelApp().run()
