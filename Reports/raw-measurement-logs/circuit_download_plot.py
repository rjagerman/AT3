#!/usr/bin/env python
import re
import matplotlib.pyplot as plt

datapoints = []
f = open('anontunnel_log_creating_circuits.txt')

for line1 in f:
    line2 = f.next()

    firstPercentage = 0
    secondsPercentage = 0

    for col in line1.split():
        if '%' in col:
            firstPercentage = int(col.strip('%'))

    for col in line2.split():
        if '%' in col:
            secondsPercentage = int(col.strip('%'))

    datapoints.append(firstPercentage+secondsPercentage)

plt.title('AT3 CPU Usage')
plt.xlabel('Running time in seconds')
plt.ylabel('CPU usage in percentage')
plt.xlim([0,100])
plt.ylim([0,100])
plt.plot(datapoints, marker='o', mfc='none', linestyle='-') 
plt.show()

f.close()
