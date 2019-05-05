#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:03:49 2019

@author: rudresh

"""
GBL = ["Gopal","Pune",7, 27,5.6] # List 
#print(type(GBL))
GBL[1] = "Nanded"
print(GBL)
GBD = {"name":"Gopal","city":"Pune","exp":7,"age":27,"height":5.6} #Dict
#print(type(GBD))
GBD["city"]="Nanded"
print(list(GBD))
GBT = ("Gopal","Pune",7,27,5.6) #tuple
#print(type(GBT))
#GBT[1]="Nanded"
print(GBT)

GBTL = list(GBT)
GBTL[1]="Nanded";
GBT = tuple(GBTL)
print(GBT)

li = ["A","B","C","D","E","F"]

'''for x in li[::-1]:
    print(x)
'''

















