#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:46:20 2024

@author: marcus
"""

import datetime as dt
from urllib import request
import time


# System time
def get_SystemTime():
    return time.asctime()

# Computer Name
def get_ComputerName():
    ## get the hostname here!!
    return 

# IP-address
def get_IPAddress():
    pass

# MAC-address
# Processor Model
# OperatingSystem
    
# Internet connection speed
def speedtester():
    ## Create a Speedtester
    
    ## start a timer / get current time
    dl_start = time.time()
    #print(dl_start)
    
    ### Download a file
    
    dl_file = "https://github.com/Mherstik/Automation_Trainee_Nov2024/raw/refs/heads/main/20MB.zip"
    
    ## download the file
    ## using a WITH to have it not stored permanently.
    with request.urlopen(dl_file) as response:
        response.read()
    
    ## stop the timer
    dl_stop = time.time() # dt.datetime.now(tz=None)
    #print(dl_stop)
    
    # Calculate time to download.
    dl_delta = dl_stop - dl_start
    #print(dl_delta)
    
    ## Convert the time to Mbps
    # speed = filesize / downloadtime
    speed = (20 * 8 ) / dl_delta
    return speed


    # • Active ports
    
    
currentTime = get_SystemTime()

speed = speedtester()
compName = get_ComputerName()

print(currentTime, speed,compName)    
    
    
