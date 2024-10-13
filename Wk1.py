#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:06:16 2024

@author: marcus
"""

# Greetings
print("Hi there... let's find out a little about you.")

#    ask your name
name = input("What is your name: ")

#   say Hello to you
print("Hello", name)

#    ask your age today
# age = input("How old are you: ")
# print("Age is", type(age))
# change the type
# age = int(age)

while True:
    age = input("How old are you: ")
    try:
        age = int(age)
        if age > 100 or age < 0:
            print("Are you sure that's your age?")
            continue
        break
    except:
        print("That was invalid. Try again.")


# print("Age is", type(age))
# print("Age is", age)


#    then print "your age next year this time will be" and add 1 to the age.
print("Next year you will be", int(age) + 1)

i = 0
while i < 10:
    print(i)
    i = i + 1

name = ["John", "Mary", "Peter", "Marianne", "Jacob", 21]
print(type(name))
print(name)
print("The list is ", len(name), "long")
for each in name:
    print(type(each))
    
mytuple = ("car", "plane", "ship", "bus")
secondtuple = ("John", "Mary", "Peter", "Marianne", "Jacob")
#print(mytuple)
# for each in mytuple:
#     print(type(each))
# mylist = ["car", "plane", "ship", "bus"]
# print(mylist)

print(mytuple + secondtuple)

myset= {"car", "plane", "ship", "bus", "plane"}
print(myset)
