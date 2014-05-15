from anontunnel.atunnel import AnonTunnel
from anontunnel.community import ProxyCommunity, ProxySettings

class AnonTunnelService():

    def startService(self):
        print 'Starting anon tunnel'
        
        socks5_port = None
        proxy_settings = ProxySettings()
        crawl = False

        self.anon_tunnel = AnonTunnel(socks5_port, proxy_settings, crawl)
        self.anon_tunnel.start()

    def stopService(self):
        print 'Stopping anon tunnel'
        self.anon_tunnel.stop()
    
if __name__ == '__main__':
    ats = AnonTunnelService()
    ats.startService()
