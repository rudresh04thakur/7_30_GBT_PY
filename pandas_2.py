#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 08:45:22 2019

@author: rudresh
"""

import pandas as pd

class Customer:
    def __init__(self):
        self.dict = {"name":[],"age":[],"contact":[],"address":[]}
    def getInfo(self):
        self.name = input("Enter name")
        self.age = input("Enter age")
        self.contact = input("Enter contact")
        self.address = input("Enter Address")
    def printInfo(self):
        print(self.name,self.age,self.contact,self.address)
        
    def makeDic(self):
        self.dict['name'].append(self.name)
        self.dict['age'].append(self.age)
        self.dict['contact'].append(self.contact)
        self.dict['address'].append(self.address)

    def getDict(self):
        return self.dict
    
class CSV:
   def Save(self,dic):
       df = pd.DataFrame(dic)
       df.to_csv("cutomer.csv")
        
if __name__=="__main__":
    n = int(input("Enter Number of Customer"))
    c = Customer()
    while(n>0):
        c.getInfo()
        c.makeDic()
        n-=1
    CSV.Save(CSV,c.getDict())
        
