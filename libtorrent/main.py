import libtorrent as lt
import time
import sys

ses = lt.session()
ses.listen_on(6881, 6891)

info = lt.torrent_info("/storage/sdcard0/Torrents/ubuntu-14.04-desktop-i386.iso.torrent")
h = ses.add_torrent({'ti': info, 'save_path': '/storage/sdcard0/Torrents/'})
print 'starting', h.name()

while (not h.is_seed()):
   s = h.status()

   state_str = ['queued', 'checking', 'downloading metadata', \
      'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']
   print('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d seeds: %d) %s' % \
      (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
      s.num_peers, s.num_seeds, state_str[s.state]))

   time.sleep(1)

print h.name(), 'complete'
