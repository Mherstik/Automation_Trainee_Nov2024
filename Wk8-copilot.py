#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:12:40 2024

@author: marcus
"""

import csv
import socket
import platform
import psutil
import subprocess
from datetime import datetime

def get_system_info():
    system_info = {
        "Computer Name": socket.gethostname(),
        "IP-address": socket.gethostbyname(socket.gethostname()),
        "MAC-address": ':'.join(['{:02x}'.format((psutil.net_if_addrs()['Wi-Fi'][0].address[n] & 0xff)) for n in range(6)]),
        "Processor Model": platform.processor(),
        "Operating System": platform.system() + " " + platform.release(),
        "System time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Internet connection speed": get_internet_speed(),
        "Active ports": get_active_ports()
    }
    return system_info

def get_internet_speed():
    try:
        result = subprocess.run(['speedtest-cli', '--simple'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        return result.split('\n')[2].split()[1] + " Mbps"
    except Exception as e:
        return "Error: " + str(e)

def get_active_ports():
    if platform.system() == "Windows":
        command = "netstat -an"
    else:
        command = "ss -tuln"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
    return result

def update_csv(file_path, system_info):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=system_info.keys())
        writer.writeheader()
        writer.writerow(system_info)

if __name__ == "__main__":
    file_path = "system_info.csv"
    system_info = get_system_info()
    update_csv(file_path, system_info)
