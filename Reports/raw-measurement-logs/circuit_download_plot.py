#!/usr/bin/env python
import re
import matplotlib.pyplot as plt

# Anonmode false - download rates
datapoints = []
f = open('new_anontunnel_anonmode_false_download.txt')

for line in f:
    download_rate = float(line.split()[3])
    datapoints.append(download_rate)

f.close()

plt.figure(0)
plt.title('AT3 Anonmode False - Download rate in KB/s')
plt.xlabel('Running time in seconds')
plt.ylabel('Download rate in KB/s')
plt.plot(datapoints, linestyle='-') 


# Anonmode false - CPU usage
datapoints = []
f = open('new_anontunnel_anonmode_false_cpu.txt')

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

plt.figure(1)
plt.title('AT3 CPU Usage when downloading with Anonmode off')
plt.xlabel('Running time in seconds')
plt.ylabel('CPU usage in percentage')
plt.xlim([0,100])
plt.ylim([0,100])
plt.plot(datapoints, linestyle='-') 

f.close()

# 1 hop 1 circuit - download rates
datapoints = []
f = open('new_anontunnel_1_hop_1_circuit.txt')

for line in f:
    download_rate = float(line.split()[3])
    datapoints.append(download_rate)

f.close()

plt.figure(2)
plt.title('AT3 1 hop 1 circuit - Download rate in KB/s')
plt.xlabel('Running time in seconds')
plt.ylabel('Download rate in KB/s')
plt.plot(datapoints, linestyle='-') 


# Anonmode false - CPU usage
datapoints = []
f = open('new_anontunnel_1_hop_1_circuit_cpu.txt')

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

plt.figure(3)
plt.title('AT3 CPU Usage when downloading with 1 hop and 1 circuit')
plt.xlabel('Running time in seconds')
plt.ylabel('CPU usage in percentage')
plt.xlim([0,100])
plt.ylim([0,100])
plt.plot(datapoints, linestyle='-') 

f.close()

# 1 hop 1 circuit - download rates
datapoints = []
f = open('new_anontunnel_1_hop_3_circuit.txt')

for line in f:
    download_rate = float(line.split()[3])
    datapoints.append(download_rate)

f.close()

plt.figure(4)
plt.title('AT3 1 hop 3 circuits - Download rate in KB/s')
plt.xlabel('Running time in seconds')
plt.ylabel('Download rate in KB/s')
plt.plot(datapoints, linestyle='-') 


# 1 hop 3 circuit- CPU usage
datapoints = []
f = open('new_anontunnel_1_hop_3_circuit_cpu.txt')

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

plt.figure(5)
plt.title('AT3 CPU Usage when downloading with 1 hop and 3 circuits')
plt.xlabel('Running time in seconds')
plt.ylabel('CPU usage in percentage')
plt.xlim([0,100])
plt.ylim([0,100])
plt.plot(datapoints, linestyle='-') 

f.close()

# 3 hops 1 circuit - download rates
datapoints = []
f = open('new_anontunnel_3_hop_1_circuit.txt')

for line in f:
    download_rate = float(line.split()[3])
    datapoints.append(download_rate)

f.close()

plt.figure(6)
plt.title('AT3 3 hops 1 circuit - Download rate in KB/s')
plt.xlabel('Running time in seconds')
plt.ylabel('Download rate in KB/s')
plt.plot(datapoints, linestyle='-') 


# 3 hops 1 circuit - CPU usage
datapoints = []
f = open('new_anontunnel_3_hop_1_circuit_cpu.txt')

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

plt.figure(7)
plt.title('AT3 CPU Usage when downloading with 3 hops and 1 circuit')
plt.xlabel('Running time in seconds')
plt.ylabel('CPU usage in percentage')
plt.xlim([0,100])
plt.ylim([0,100])
plt.plot(datapoints, linestyle='-') 

f.close()

# 3 hops 3 circuits - download rates
datapoints = []
f = open('new_anontunnel_3_hop_3_circuit.txt')

for line in f:
    download_rate = float(line.split()[3])
    datapoints.append(download_rate)

f.close()

plt.figure(8)
plt.title('AT3 3 hops 3 circuits - Download rate in KB/s')
plt.xlabel('Running time in seconds')
plt.ylabel('Download rate in KB/s')
plt.plot(datapoints, linestyle='-') 


# 3 hops 3 circuits - CPU usage
datapoints = []
f = open('new_anontunnel_3_hop_3_circuit_cpu.txt')

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

plt.figure(9)
plt.title('AT3 CPU Usage when downloading with 3 hops and 3 circuits')
plt.xlabel('Running time in seconds')
plt.ylabel('CPU usage in percentage')
plt.xlim([0,100])
plt.ylim([0,100])
plt.plot(datapoints, linestyle='-') 

f.close()

# Show the plots
plt.show()