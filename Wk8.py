#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:46:20 2024

@author: marcus
"""

import datetime as dt
from urllib import request
import time
import socket
import os.path
import csv
import re
import uuid


# System time
def get_SystemTime():
    return time.asctime()

# Computer Name
def get_ComputerName():
    ## get the hostname here!!
    name = socket.gethostname()
    return name

# IP-address
def get_IPAddress():
    
    # Create a socket to connect to an external server
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # This IP address (8.8.8.8) is Google's DNS server, used just for getting the local IP
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
    except Exception as e:
        local_ip = "Unable to get IP address: " + str(e)
    finally:
        s.close()
    return local_ip

# MAC-address
def get_MACaddress():
    mac_add =  ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    return mac_add


# Processor Model
def get_Processor():
    pass

# OperatingSystem
def get_OperatingSystem():
    pass

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
print(f"Current time is {currentTime}")

speed = speedtester()
print(f"The speed is {speed}")

compName = get_ComputerName()
print(f"The computer name is {compName}")

compIP = get_IPAddress()
print(f"The computer IP address is {compIP}")

compMAC = get_MACaddress()
print(f"The MAC address is {compMAC}")
## NOT IMPLEMENTED
processor = get_Processor()
operating_system = get_OperatingSystem()


### Store the speeds in a table or file

### check if file exists.
# filename = "Week7a.csv"

# import os.path

# this checks if "anything" with that name exists
# and returns a True or False
# if os.path.exists(filename):
#     print("Something exists") 
# else:
#     print("False")

# this checks if a directory exists 
# and returns a True or False
# if os.path.isdir("Week7"):
#     print("Folder exists")
# else:
#     print("Folder is not there")

# this checks if a file with that name exists
# and returns a True or False
# if os.path.isfile(filename):
#     print("File exists")
# else:
#     print("File does not exist")


## if file DOES NOT exist... write the headers
## if file exists... move to adding speed to file
## else add speed to file
print(currentTime, speed, compName)    

filename = "Week8.csv"
if os.path.exists(filename):
    print("File exists.\nSkipping headers")
    f = open(filename, "a")
else:
    f = open(filename, "a")
    print("File does not exist.\nWriting headers")
    f.write("Time/Date,Hostname,Speed\n")  ## make this optional

f.write(f"{currentTime},")
f.write(compName + ",")
f.write(str(speed) + '\n')
f.close()



    
    
