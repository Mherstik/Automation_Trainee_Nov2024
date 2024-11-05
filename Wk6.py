#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 13:07:23 2024

@author: marcus
"""

import datetime as dt
from urllib import request

import time
# print(f"Time is {time.time()}")
# print(f"GM Time is {time.gmtime()}")
# print(f"C Time is {time.ctime()}")

## Create a Speedtester

## start a timer / get current time
# dl_start = dt.datetime.now(tz=None)  # changed to time.time
dl_start = time.time()
print(dl_start)

### Download a file

dl_file = "https://github.com/Mherstik/Automation_Trainee_Nov2024/raw/refs/heads/main/20MB.zip"

## download the file??
with request.urlopen(dl_file) as response:
    response.read()


## stop the timer
dl_stop = time.time() # dt.datetime.now(tz=None)
print(dl_stop)

# Calculate time to download.
dl_delta = dl_stop - dl_start
print(dl_delta)

## Convert the time to Mbps
# speed = filesize / downloadtime
speed = 
print(f"Your internet is running at {speed}Mbps")

## 10MB file =  80 Mbits = factor of 8
# 20MB = 160 Mbits

