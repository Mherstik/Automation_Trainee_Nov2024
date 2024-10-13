#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:53:36 2024

@author: marcus
"""

grade = int(input("Gimme a grade: "))

def grading(marks):
    if (marks > 100):
    	print("Out of range 0-100")
    elif (marks < 50): 
    	print("F")
    elif (marks < 65):
    	print("P")
    elif (marks < 75):
    	print("C")
    elif (marks < 85):
    	print("D")
    else:
    	print("HD")
        
grading(grade)
