import os

#adjust the PYTHON_EGG_CACHE
os.environ["PYTHON_EGG_CACHE"] = "/data/data/com.AT3.anontunnel/cache"

print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
print os.getcwd()
print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

from anontunnel.atunnel import AnonTunnel
from anontunnel.community import ProxyCommunity, ProxySettings

class AnonTunnelService():

    def startService(self):
        print 'Starting the anonymous tunnels...'
        
        socks5_port = None
        proxy_settings = ProxySettings()
        crawl = False

        self.anon_tunnel = AnonTunnel(socks5_port, proxy_settings, crawl)
        self.anon_tunnel.start()

    def stopService(self):
        print 'Stopping the anonymous tunnels...'
        self.anon_tunnel.stop()
    
if __name__ == '__main__':
    ats = AnonTunnelService()
    ats.startService()
