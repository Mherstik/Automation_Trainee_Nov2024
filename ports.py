#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:14:50 2024

@author: marcus
"""

import psutil
import csv
import time
import os

currentTime = time.ctime()

def getActivePorts():
    active_ports = []
    connections = psutil.net_connections(kind='tcp4')  # Fetch TCP connections
    for conn in connections:
        if conn.status == 'LISTEN':
            active_ports.append(conn.laddr.port)
    return active_ports

portListen = getActivePorts()
portListen = str(portListen).strip('[]').replace(',', ';')

fileName = input("Gimme a filename: ")
isFile = os.path.isfile(fileName)


header = ['Time', 'ports']
def writeHeader():
    with open(fileName, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(header)
    print("Headers written.\nNow extracting data from PC")

if isFile == True:
    print("File exists")  #... extracting data from PC")
    fileKeep = input("Want to Delete or Continue (C/D)?")
    if fileKeep.upper() == "D" or fileKeep.upper() == "DELETE":
        print("Deleting file")
        os.remove(fileName)
        writeHeader()
    else:
        print("Continuing")
else:
    print("File not found... writing headers.")
    writeHeader()


data = [currentTime, portListen]

### NICER OPENING
def readCSVFile():
    with open(fileName, mode='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            print(lines)

with open(fileName, mode='a') as file:
    writer = csv.writer(file)
    writer.writerow(data)



readCSVFile()
