#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 09:10:20 2019

@author: rudresh
"""
n = int(input())
s = 0
while(n>0):
    t = n%10
    if(t%3==0 or t%5==0):
        s += t
    n//=10
print("Sum is ",s)

