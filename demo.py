#!/usr/bin/env python
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import sys
import re
import json
from subprocess import Popen, PIPE
from collections import deque

# Prepare data
count = 0
cpu = deque([0, 0, 0, 0, 0])
speed = deque([0.0, 0.0, 0.0])

# Prepare plotting
matplotlib.rcParams['toolbar'] = 'None'
matplotlib.rcParams.update({'font.size': 24})
plt.get_current_fig_manager().full_screen_toggle()
plt.ion()
figure = plt.figure(1, figsize=(12, 7), dpi=90)
gs = gridspec.GridSpec(2, 2, height_ratios=[1,5])
plots = {'progress': figure.add_subplot(gs[0, 0:2]),
         'cpu': figure.add_subplot(gs[1, 0]),
         'speed': figure.add_subplot(gs[1, 1])}
figure.subplots_adjust(wspace=0.32, hspace=0.4, left=0.08, right=0.97, bottom=0.09, top=0.90)
plots['cpu'].set_autoscale_on(True)
plots['cpu'].axis([0,5,0,100])
plots['cpu'].set_xlabel('Time in seconds (s)')
plots['cpu'].set_ylabel('CPU usage (%)')
plots['speed'].set_autoscale_on(True)
plots['speed'].set_xlabel('Time in seconds (s)')
plots['speed'].set_ylabel('Download speed (KB/s)')
plots['progress'].set_xlim([0, 100])
plots['progress'].set_xlabel('Download completed (%)')
plots['progress'].set_yticks([])
plots['progress'].set_title('AT3', y=1.3)
figure.show()

def update_progress_plot(data):
    global plots, count
    plots['progress'].barh(0, [data['progress']], 1, color='b')
    if data['progress'] < 100.0:
        plots['progress'].set_title('Currently using %d circuits' % data['circuits'], y=1.3, size='x-large')
    else:
        plots['progress'].set_title('Done!', y=1.3, size='x-large')


def update_cpu_plot(data):
    global cpu, plots, count

    prev, now = move_average(cpu, data['cpu']/2.0)

    plots['cpu'].plot([count-1, count], [prev, now], color='black', linewidth=5.0)
    plots['cpu'].set_autoscale_on(True)
    plots['cpu'].autoscale_view(scaley=False, tight=False)
    plots['cpu'].get_axes().set_ylim(0, 100)


def update_download_speed_plot(data):
    global speed, plots, count

    prev, now = move_average(speed, data['speed'])

    plots['speed'].plot([count-1, count], [prev, now], color='black', linewidth=5.0)
    plots['speed'].set_autoscale_on(True)
    plots['speed'].autoscale_view(tight=False)


def move_average(data, new_entry):
    prev_average = sum(data) / len(data)
    data.popleft()
    data.append(new_entry)
    average = sum(data) / len(data)
    return (prev_average, average)


while True:
    line = sys.stdin.readline()
    if "I/python" in line and "REALTIME" in line:
        count += 1
        m = re.match(".*REALTIME (.*)", line)
        data = json.loads(m.groups()[0].rstrip("\r"))
        if data['progress'] >= 100.0:
            data['speed'] = 0.0
        #data[0] /= 2.0

        update_cpu_plot(data)
        update_progress_plot(data)
        if data['progress'] > 0.0:
            update_download_speed_plot(data)

        plt.draw()
        time.sleep(0.05)
        # prevdata = data



#while True:
#    plt.
#    plt.draw()
#    time.sleep(0.05)

