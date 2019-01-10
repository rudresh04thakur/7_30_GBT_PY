# -*- coding: utf-8 -*-
"""
Spyder Editor
Find the Prime Number 
Author: Gopal L Thakur
CopyRight: GB Tech
Date: 09/01/2019
"""
number = int(input("Enter 1st Number"))
#print(type(number))
i = 2
flag = True
while(i<number and flag==True):
    if(number%i==0):
        flag = False
    i+=1
if(flag==True):
    print("its a prime number")
else:
    print("not prime number")
    