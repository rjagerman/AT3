import kivy
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.app import App
import os

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

class AnonTunnelScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(AnonTunnelScreen, self).__init__(**kwargs)

        # redirect the stdout to the log_textview
        import sys
        sys.stdout = StdoutRedirector(self.log_textview)

class AnonTunnelApp(App):
    def build(self):

        if platform == 'android':
            from android import AndroidService
            service = AndroidService('Anon Tunnel Service', 'Runs the anontunnels in the background.')
            service.start('AnonTunnel Service started')
            self.service = service

        return AnonTunnelScreen()

if __name__ == '__main__':
    AnonTunnelApp().run()
