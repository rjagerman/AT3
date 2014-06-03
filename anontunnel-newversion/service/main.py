import os
from kivy.lib import osc
import logging
import logging.config

class IORedirector(object): # A general class for redirecting I/O to this Text widget.
    def __init__(self):
        pass

class StdoutRedirector(IORedirector): # A class for redirecting stdout to this Text widget.
    def write(self,str):
        osc.sendMsg('/log', [str], port=3002)

#adjust the PYTHON_EGG_CACHE
os.environ["PYTHON_EGG_CACHE"] = "/data/data/com.devos.anontunnel1/cache"

#adjust the TRIBLER_STATE_DIR
os.environ['TRIBLER_STATE_DIR'] = "/storage/emulated/0/com.devos.anontunnel1/.Tribler"
#os.environ['TRIBLER_STATE_DIR'] = "/storage/sdcard0/com.devos.anontunnel1/.Tribler"

from Tribler.community.anontunnel.atunnel import AnonTunnel
from Tribler.community.anontunnel.community import ProxyCommunity, ProxySettings

class AnonTunnelService():


    def startService(self):

        # redirect the stdout to the log_textview
        #sys.stdout = StdoutRedirector()

        # redirect logger to stdout
        #root = logging.getLogger()
        #root.setLevel(logging.DEBUG)
        #ch = logging.StreamHandler(sys.stdout)
        #ch.setLevel(logging.DEBUG)
        #root.addHandler(ch)

        print 'Starting the anonymous tunnels...'
        
        socks5_port = None
        proxy_settings = ProxySettings()
        crawl = False

        self.anon_tunnel = AnonTunnel(socks5_port, proxy_settings, crawl)
        self.anon_tunnel.run()

        from time import sleep
        while True:
            sleep(1)

    def stopService(self):
        print 'Stopping the anonymous tunnels...'
        self.anon_tunnel.stop()
    
if __name__ == '__main__':
    osc.init()
    oscid = osc.listen(ipAddr='0.0.0.0', port=3000)
    ats = AnonTunnelService()
    ats.startService()