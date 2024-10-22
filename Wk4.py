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

loopCount = 1
maxNum = 100

# Computer guesses
compNum = random.randint(0,maxNum)
print(compNum)


# Get user number
## below doesn't work because INPUT can only have 1 thing
#userNum = input("Pick a number between 0 to ", maxNum)

#print("Pick a number between 0 to" + str(maxNum)) 

def userChoice(): 
    ## Check to make sure it's a number
    global userNum
    while True:
        userNum = input(f"Pick a number between 0 & {maxNum}: ")
        # if userNum.isdigit():
        #     # print("It's a number")
        #     if int(userNum) < 0 or int(userNum) > maxNum:
        #         print("Invalid number.")
        #         continue
        #     else:
        #         break
        #     # print(loopCount)
        #     # loopCount = loopCount + 1
        # else:
        #     print("It's not a number")
        #     continue
        try:
            usernum = int(userNum)
            if int(userNum) < 0 or int(userNum) > maxNum:
                print("Invalid number.")
                continue
            break
        except:
            print("It's not a number")
            continue
            

### CONDUCT TESTS for higher/lower



# Options: correct, higher or lower

while loopCount < 4:
    userChoice()
    if int(userNum) == compNum:
        print("YEAH!!! You got it.")
        break
    else:
        print("Wrong!!!")
        # print("You have made" + i + "attempts")  ## doesn't work
        # print("You have made" + str(i) + "attempts")
        if int(userNum) > compNum:
            print("Too High")
        else: 
            print("Too low")
        print(f"You have made {loopCount} attempts") 
        loopCount = loopCount + 1
        
    # if user > computer
    #      tell lower
    # if user < computer
    #      tell higher



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
