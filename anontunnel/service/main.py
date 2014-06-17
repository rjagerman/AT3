import os
try:
    import android
    os.environ["PYTHON_EGG_CACHE"] = "/data/data/org.tribler.at3.anontunnel/cache"
    os.environ['TRIBLER_STATE_DIR'] = "/sdcard/org.tribler.at3.anontunnel/.tribler"
except ImportError:
    os.environ['TRIBLER_STATE_DIR'] = "./.tribler"
import logging
import logging.config
import sys
import Tribler
sys.path.append(os.path.dirname(Tribler.__file__))
from time import sleep
from kivy.lib import osc
from kivy.clock import Clock
from Tribler.community.anontunnel.community import ProxySettings
from Tribler.community.anontunnel.atunnel import AnonTunnel
from threading import Timer
import psutil


#class StdoutRedirector(object): # A class for redirecting stdout to this Text widget.
#    def __init__(self):
#        pass
#    def write(self, string):
#        sys.stdout.write(string)
#        sys.stdout.flush()
#        osc.sendMsg('/logger', [string], ipAddr='127.0.0.1', port=9000)


class AnonTunnelService():
    """
    The service that runs the anontunnels
    """

    def setup_logging(self):
        """
        Sets up the log handler
        """
        self.log = logging.getLogger()
        self.log.setLevel(logging.INFO)
        log_handlers = [h for h in self.log.handlers]
        for log_handler in log_handlers:
            self.log.removeHandler(log_handler)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO)
        ch.setFormatter(logging.Formatter('%(levelname)-8s %(message)s'))
        self.log.addHandler(ch)

    def start(self, blocking=True):
        """
        Starts the anontunnel service
        :param blocking: True if this method should block or False to continue execution
        """

        self.setup_logging()
        self.log.info('Starting the anonymous tunnels...')
        
        socks5_port = None
        proxy_settings = ProxySettings()
        crawl = False

        self.anon_tunnel = AnonTunnel(socks5_port, proxy_settings, crawl)
        self.anon_tunnel.run()

        self.status(setup=True)

        while blocking:
            osc.readQueue()
            sleep(1)

    def status(self, setup=False, stop=False):
        """
        Runs status updates from the anontunnels
        """
        if setup:
            self.running_updates = True
        if stop:
            self.running_updates = False
        if self.running_updates:
            self.timer = Timer(1, self.status).start()
            status = self.anon_tunnel.status()
            cpu = ', '.join([str(abs(core)) for core in psutil.cpu_percent(percpu=True)])
            array_status = [status['circuits'],
                            status['relays'],
                            status['enter'],
                            status['relay'],
                            status['exit'],
                            status['download_speed'],
                            status['download_progress'],
                            cpu]
            osc.sendMsg('/status', array_status, ipAddr='127.0.0.1', port=9000)

    def stop(self):
        """
        Stops the anontunnel service
        """
        self.log.info('Stopping the anonymous tunnels...')
        self.status(stop=True)
        try:
            self.anon_tunnel.stop()
        except Exception as e:
            self.log.error(e.message)

if __name__ == '__main__':
    osc.init()
    # oscid = osc.listen(ipAddr='0.0.0.0', port=3000)
    ats = AnonTunnelService()
    ats.start()
