import logging
import logging.config
import os

import kivy
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.app import App
import sys

#adjust the PYTHON_EGG_CACHE
os.environ["PYTHON_EGG_CACHE"] = "/data/data/com.devos.anontunnel1/cache"

from anontunnel.atunnel import AnonTunnel

"""
AnonTunnel CLI interface
"""

print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
print os.getcwd()
print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

from anontunnel.community import ProxyCommunity, \
    ProxySettings

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

	tunnelStarted = False

	def __init__(self, **kwargs):
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
		if self.tunnelStarted == True:
			print 'stopping anon tunnel'
			self.tunnel_togglebutton.text = 'Off'
			self.tunnelStarted = False

			self.anon_tunnel.stop()
		else:
			print 'starting anon tunnel'
			self.tunnel_togglebutton.text = 'On'
			self.tunnelStarted = True

			socks5_port = None
			proxy_settings = ProxySettings()
			crawl = False

			self.anon_tunnel = AnonTunnel(socks5_port, proxy_settings, crawl)
			self.anon_tunnel.start()

class AnonTunnelApp(App):
    def build(self):
        return AnonTunnelScreen()

if __name__ == '__main__':
    AnonTunnelApp().run()
