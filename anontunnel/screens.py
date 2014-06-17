from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.lib import osc
from kivy.uix.anchorlayout import AnchorLayout
import logging


class ScrollableLabel(ScrollView):
    """
    A scrollable text label
    """
    text = StringProperty('')


class AnonTunnelScreen(Screen):
    """
    The main screen of the application
    """

    def __init__(self, **kwargs):
        self.is_running = False
        self.service = None
        super(AnonTunnelScreen, self).__init__(**kwargs)

    def stop_anontunnel(self):
        """
        Stops the anontunnel
        """
        if self.is_running:
            self.tunnel_togglebutton.text = 'Off'
            self.status_text.text = 'No anontunnels running...'
            self.status_view.opacity = 0.0
            self.download_text.text = 'Currently inactive'
            self.download_view.opacity = 0.0
            self.is_running = False
            self.service.stop()

    def start_anontunnel(self):
        """
        Starts the anontunnel
        """
        if not self.is_running:
            self.tunnel_togglebutton.text = 'On'
            self.status_text.text = 'Running anontunnels'
            self.status_view.opacity = 1.0
            self.download_text.text = 'Currently downloading a 50M test file'
            self.download_view.opacity = 1.0
            self.is_running = True
            try:
                self.start_anontunnel_android()
            except ImportError:
                self.start_anontunnel_thread()
            
    def start_anontunnel_android(self):
        """
        Starts the anontunnel as an android service
        """
        from android import AndroidService
        service = AndroidService('Anonymous downloading Service', 'Anonymous tunnels are running...')
        service.start('Anonymous tunnels service started')
        self.service = service

    def start_anontunnel_thread(self):
        """
        Starts the anontunnel as a thread
        """
        from service.main import AnonTunnelService
        self.service = AnonTunnelService()
        self.service.start(blocking=False)

    def toggle_anontunnel(self):
        """
        Toggles the anon tunnel on/off
        """
        if not self.is_running:
            self.start_anontunnel()
        else:
            self.stop_anontunnel()


class SettingsScreen(Screen):
    """
    The settings screen is currently a mockup so it is recognized by the screen manager
    """
    pass
