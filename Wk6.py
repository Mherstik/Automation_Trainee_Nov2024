#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 13:07:23 2024

@author: marcus
"""

import datetime as dt

## Create a Speedtester

## start a timer / get current time
dl_start = dt.datetime.now(tz=None)
print(dl_start)
### Download a file

pause = input("Press enter to stop the pause")


## stop the timer
dl_stop = dt.datetime.now(tz=None)
print(dl_stop)

# Calculate time to download.
dl_delta = dl_stop - dl_start
print(dl_delta)

## Convert the time to Mbps

## 10MB file =  80 Mbits = factor of 8
