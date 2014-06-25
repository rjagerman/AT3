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
from time import sleep, clock
from kivy.lib import osc
from kivy.clock import Clock
from Tribler.community.anontunnel.community import ProxySettings
from Tribler.community.anontunnel.atunnel import AnonTunnel
from threading import Timer
import psutil
import pickle
import base64


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

        self.tribler_start = clock()
        self.cpu_status(setup=True)

        self.NRHOPS = 3
        self.NRCIRCUITS = 3

        self.anon_tunnel = AnonTunnel(socks5_port, proxy_settings, crawl, hops=self.NRHOPS, circuits=self.NRCIRCUITS)
        self.anon_tunnel.run()

        self.cpu_status(stop=True)
        self.tribler_end = clock()

        # Store the basic setup
        self.startup_cpu_benchmark = self.cpu_benchmark

        # During download, run the cpu_status 
        self.download_start = clock()
        self.cpu_status(setup=True)
        self.status(setup=True)

        while blocking:
            osc.readQueue()
            sleep(1)

    def cpu_status(self, setup=False, stop=False):
        if setup:
            self.running_cpu_updates = True
            self.cpu_benchmark = []
        if stop:
            self.running_cpu_updates = False
            if self.cpu_timer is not None:
                self.cpu_timer.stop()
        if self.running_cpu_updates:
            self.cpu_timer = Timer(1, self.cpu_status).start()
            self.cpu_usage = psutil.cpu_percent(percpu=True)
            self.cpu_benchmark.append((clock(), sum(self.cpu_usage)/4.0))


    def status(self, setup=False, stop=False):
        """
        Runs status updates from the anontunnels
        """
        if setup:
            self.running_updates = True
            self.download_benchmark = []
            self.download_first_byte = None
            self.printed_results = False
        if stop:
            self.running_updates = False
            if self.timer is not None:
                self.timer.stop()
        if self.running_updates:
            self.timer = Timer(1, self.status).start()
            status = self.anon_tunnel.status()
            cpu = ', '.join([str(abs(core)) for core in self.cpu_usage])
            print 'REALTIME {"cpu": %f, "speed": %f, "progress": %f, "circuits": %d}' % (sum(self.cpu_usage), status['download_speed'], status['download_progress'], status['circuits'])
            array_status = [status['circuits'],
                            status['relays'],
                            status['enter'],
                            status['relay'],
                            status['exit'],
                            status['download_speed'],
                            status['download_progress'],
                            cpu]
            self.download_benchmark.append((clock(), status['download_speed']))
            if status['download_speed'] > 0.0 and self.download_first_byte is None:
                self.download_first_byte = clock()
            if status['download_progress'] >= 100.0 and not self.printed_results:
                self.printed_results = True
                self.download_end = clock()
                self.output = {'timings':
                                  {'tribler_start': self.tribler_start,
                                   'tribler_end': self.tribler_end,
                                   'download_start': self.download_start,
                                   'download_first_byte': self.download_first_byte,
                                   'download_end': self.download_end},
                               'cpu': self.cpu_benchmark,
                               'speed': self.download_benchmark}
                results_file = open('/sdcard/experiments/%d_hops_%d_circuits.pickle' % (self.NRHOPS, self.NRCIRCUITS), 'w')
                results_file.write(base64.urlsafe_b64encode(pickle.dumps(self.output)))
                results_file.close()

                print '--- IMPORTANT TIMESTAMPS ---'
                print 'Start Tribler/Dispersy startup at    %.2f' % self.tribler_start
                print 'Finished Tribler/Dispersy startup at %.2f' % self.tribler_end
                print 'Start download                       %.2f' % self.download_start
                print 'First byte downloaded                %.2f' % self.download_first_byte
                print 'Finished download                    %.2f' % self.download_end
                print '--- CPU ---'
                print self.cpu_benchmark
                print '--- KB/S ---'
                print self.download_benchmark
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
