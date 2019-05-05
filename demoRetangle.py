#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 08:39:12 2019

@author: rudresh
"""

#from retangleModel import retangle as rt
import retangleModel as rt

import pandas as pd
#rt.setCoordinate(rt,20,20)
#print(rt.getArea(rt))

rt.retangle.setCoordinate(rt.retangle,20,20);
print("Retangle Area is %d"%rt.retangle.getArea(rt.retangle))
rt.circle.setCoordinate(rt.circle,15);
print("Circle Area is %d"%rt.circle.getArea(rt.circle))

d = {
     "name":["Gopal","Ganesh","Mahesh"],
     "age":[28,24,54],
     "contact":[123,321,432]
    }

#print(pd.DataFrame(d).to_csv("demo.csv"))
df = pd.DataFrame(d)
    #print(df[1:2,0:1])
#print(pd.read_csv("newcsv3.csv"))
#print(pd.DataFrame(d,columns=["name","contact"]));
#print(pd.Series(d,index=['name']))