#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 11:40:44 2019

@author: rudresh
"""

class Demo:
    count = 1
    def __init__(self):
        pass
    
    @staticmethod
    def counter():
        Demo.count += 1
        return Demo.count
    
        
d = Demo()
print(d.counter())

i = Demo()
print(i.counter())


echo "# 1_00_GBT_MEAN" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/rudresh04thakur/1_00_GBT_MEAN.git
git push -u origin master