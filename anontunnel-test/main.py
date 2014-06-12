import kivy
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.app import App
from time import sleep
import threading
import signal

# import tribler
import sys
import os

try:
    import android
    os.environ["PYTHON_EGG_CACHE"] = "/data/data/org.tribler.at3.anontunneltest/cache"
    os.environ['TRIBLER_STATE_DIR'] = "/sdcard/org.tribler.at3.anontunneltest/.tribler"
except ImportError:
    sys.path.append('/home/martijn/Documenten/rolf-tribler')
    os.environ['TRIBLER_STATE_DIR'] = "/home/martijn/Documenten/.Tribler"

from Tribler.community.anontunnel.community import ProxySettings
from Tribler.community.anontunnel.atunnel import AnonTunnel

socks5_port = None
proxy_settings = ProxySettings()
crawl = False

anon_tunnel = AnonTunnel(socks5_port, proxy_settings, crawl)
anon_tunnel.run()

def check_status():
    if anon_tunnel.community and anon_tunnel.community.libtorrenttest.download_finished_at:
        print 'TEST SUCCESSFUL'
        os.kill(os.getpid(), signal.SIGINT)
    threading.Timer(5, check_status).start();

Builder.load_string('''
<AnontunnelStressScreen>:
    cols: 1
    Label:
        text: 'Running ANON download test...'
''')

class AnontunnelStressScreen(GridLayout):
    check_status()

class AnontunnelStressApp(App):
    def build(self):
        return AnontunnelStressScreen()

if __name__ == '__main__':
    AnontunnelStressApp().run()
