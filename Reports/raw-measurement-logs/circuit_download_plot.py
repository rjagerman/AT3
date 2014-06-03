#!/usr/bin/env python
import re
import matplotlib.pyplot as plt

#idle
datapoints = []
f = open('anontunnel_log_idle_searching_only.txt')

double = False

for line1 in f:
    if '--' in line1:
        double = not double

    if(double):
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
    else:
        for col in line1.split():
            if '%' in col:
                datapoints.append(int(col.strip('%')))

plt.figure(0)
plt.title('AT3 CPU Usage when idle / searching only')
plt.xlabel('Running time in seconds')
plt.ylabel('CPU usage in percentage')
plt.xlim([0,100])
plt.ylim([0,100])
plt.plot(datapoints, linestyle='-') 

f.close()

# creating circuits functionality.
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

plt.figure(1)
plt.title('AT3 CPU Usage when downloading')
plt.xlabel('Running time in seconds')
plt.ylabel('CPU usage in percentage')
plt.xlim([0,100])
plt.ylim([0,100])
plt.plot(datapoints, linestyle='-') 

# Show the plots
plt.show()

f.close()
