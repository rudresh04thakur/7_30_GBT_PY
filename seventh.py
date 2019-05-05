#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 08:56:20 2019
inline for loop
@author: rudresh
"""
for x in range(0,5,):
    if(x%2 == 0):
        print(x*x)
s = ["D 0200","W 300"]

[print(x.split(" ")) for x in s ] 