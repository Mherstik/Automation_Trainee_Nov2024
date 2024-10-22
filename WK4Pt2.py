#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:46:44 2024

@author: marcus
"""


x = "hello"

i = 1
#if condition is False, AssertionError is raised:
#assert x == "goodbye", "x should be 'hello'" 
#assert x == "testing", "x should be hello - not testing"
assert x == "hello", "x should not be hello"
# breakpoint()
import logging


logging.warning("This is a warning")

# def someFunction(someInput):
#     newVariable = someInput+ 10 #this is a local variable
#     return newVariable
# print(someFunction(7))
# #print(newVariable)


# def anotherFunction():
#     global anotherVar
#     anotherVar = 2
# anotherFunction()
# print(anotherVar + 1)


### get a number from a user
# num = int(input("Give me a number: "))
## run a test and say if it's odd or even
# print(99 / 3)
# print(99 // 3) # whole number times it goes in
# print(99 % 3)  # remainder
    
def oddCheck(num):
    if num % 2 == 0:
        print("it's even")
    else:
        print("It's odd")

oddCheck(10)
oddCheck(11)
oddCheck(12)
oddCheck(13)
oddCheck(14)

i = 0
while i < 10:
    i = i + 1

    print(i)
    
x = "test"

# x = int(x)  # ValueError
# x + 1  # TypeError
try: 
    #x = int(x)
    t = 4 / 0
    #x + 1
except TypeError:
    print("This was a type error")
except ValueError:
    print("This was a value error")
except:
    print("Didn't do something else")
