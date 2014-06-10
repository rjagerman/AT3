import os
try:
    import android
    os.environ["PYTHON_EGG_CACHE"] = "/data/data/org.tribler.at3.anontunnel/cache"
    os.environ['TRIBLER_STATE_DIR'] = "/sdcard/org.tribler.at3.anontunnel/.tribler"
except ImportError:
    os.environ['TRIBLER_STATE_DIR'] = "./.tribler"
import logging
import logging.config
from time import sleep
from Tribler.community.anontunnel.community import ProxySettings
from Tribler.community.anontunnel.atunnel import AnonTunnel

# class IORedirector(object): # A general class for redirecting I/O to this Text widget.
#     def __init__(self):
#         pass

# class StdoutRedirector(IORedirector): # A class for redirecting stdout to this Text widget.
#     def write(self,str):
#         osc.sendMsg('/log', [str], port=3002)

class AnonTunnelService():
    """
    The service that runs the anontunnels
    """

    def start(self, blocking=True):
        """
        Starts the anontunnel service
        :param blocking: True if this method should block or False to continue execution
        """

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

        while blocking:
            sleep(1)

    def stop(self):
        """
        Stops the anontunnel service
        """
        print 'Stopping the anonymous tunnels...'
        self.anon_tunnel.stop()

if __name__ == '__main__':
    # osc.init()
    # oscid = osc.listen(ipAddr='0.0.0.0', port=3000)
    ats = AnonTunnelService()
    ats.start()
