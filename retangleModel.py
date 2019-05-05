#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 08:32:01 2019

@author: rudresh
"""

class retangle:
    def __init__(self):
        self.lenght = 0;
        self.width = 0;
    def setCoordinate(self,l,w):
        self.lenght = l
        self.width = w
    def getArea(self):
        return (self.lenght * self.width)
    
class circle:
    def __init__(self):
        self.radius = 0;
        self.pi = 0;
    def setCoordinate(self,r,pi=3.14):
        self.radius = r
        self.pi = pi
    def getArea(self):
        return (self.radius * (self.pi**2))