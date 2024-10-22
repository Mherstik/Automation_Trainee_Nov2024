#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:13:22 2024

@author: marcus
"""

# Guessing numbers game program
# Maximum of 5 guesses
# Range of numbers (max 100)
# Computer decides a number
# User guesses
# Options: correct, higher or lower
# if user > computer
#      tell lower
# if user < computer
#      tell higher

import random

loopCount = 0
maxNum = 100

# Computer guesses
compNum = random.randint(0,maxNum)
# print(compNum)


# Get user number
userNum = input(f"Pick a number between 0 & {maxNum}: ")
#userNum = input("Pick a number between 0 to ", maxNum)
#print("Pick a number between 0 to" + str(maxNum)) 

## Check to make sure it's a number
while True:
    if userNum.isdigit():
        print("It's a number")
        if int(userNum) < 0 or int(userNum) > maxNum:
            userNum = input(f"Pick a number between 0 & {maxNum}: ")
        else:
            break
        # print(loopCount)
        # loopCount = loopCount + 1
    else:
        print("It's not a number")
        userNum = input(f"Pick a number between 0 & {maxNum}: ")


### CONDUCT TESTS for higher/lower






###############
####
####
####   PRE-CONTENT

# i = 0.0
# print(type(i))

# while i < 10:
#     i = i + 1
#     print(i)


# print("I am here")

# print("We are done")

# myList = ['Server1', 'Server2', 'Server3']
# print(myList)
# print(type(myList))
# print(myList[2])

# for each in myList:
#     print(each + " IP address check")


# myset= {"car", "plane", "skateboard", "ship", "bus"}
# print(myset)