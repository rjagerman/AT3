#!/usr/bin/env python
import re

f = open('anontunnel_log_creating_circuits.txt')

RPlotString = "plot(c("

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

	RPlotString += str(firstPercentage+secondsPercentage)+','

RPlotString = RPlotString[:-1]
RPlotString += "), type=\"o\", col=\"blue\", main=\"AT3 CPU Usage\"," + \
"xlab=\"Running time in seconds\", ylab=\"CPU usage in percentage\",  xlim=c(0, 100), ylim=c(0, 100))"

print RPlotString

f.close()
