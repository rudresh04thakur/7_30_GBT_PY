#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 08:50:02 2019
Functions
Author: Gopal L Thakur
CopyRight: GB Tech

"""

def findPrime(num):
    flag = True
    for i in range(2,num):
        if(num%i==0):
            flag = False 
    return flag

def findPrimeR(n,num):
    print(n,num)
    if(n==2):
        return True
    else:
        if(num%n==0):
            return False
        else:
            findPrimeR(n-1,num)
    



c = int(input("Enter A Number "))
print(findPrimeR(c-1,c))
#print(findPrime(int(input("Enter A Number "))))
        
        