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

def speedtester():
    ## Create a Speedtester
    
    ## start a timer / get current time
    # dl_start = dt.datetime.now(tz=None)  # changed to time.time
    dl_start = time.time()
    #print(dl_start)
    
    ### Download a file
    
    dl_file = "https://github.com/Mherstik/Automation_Trainee_Nov2024/raw/refs/heads/main/20MB.zip"
    
    ## download the file
    # response = request.urlopen(dl_file)
    
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

speed = speedtester()
print(f"Your internet is running at {speed:.2f}Mbps")

### Store the speeds in a table or file

### check if file exists.
## if file DOES NOT exist... write the headers
## if file exists... move to adding speed to file
## else add speed to file


filename = "speedtester.txt"
f = open(filename, "a")

f.write("Time/Date, Speed\n")  ## make this optional

f.write(f"{time.ctime()},")
f.write(str(speed) + "\n")
f.close()



# f2 = open(filename, "r")
# print(f2.readline())
# f2.close()

with open(filename, "r") as f:
    print(f.read())
    


