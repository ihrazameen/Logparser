#!/usr/bin/env python3

import sys
import os
import collections
import logparser



arguments = sys.argv[1:]

usage = './ipcounter.py  /path/to/access_log  number_of_results'

if len(arguments) == 2:

        logFile = arguments[0]
        maxCount = arguments[1]

        if os.path.exists(logFile) and os.path.isfile(logFile) and maxCount.isdigit():

                ipCounter = collections.Counter()
                fh = open(logFile)
                for logLine in fh:
                        ip = logparser.parser(logLine)['host']
                        ipCounter.update([ip])

                for item in ipCounter.most_common(int(maxCount)):
                        ip,hit = item
                        print('{:18} : {}'.format(ip,hit))

                fh.close()

        else:
                print(usage)
else:
        print(usage)