#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 08:44:17 2019

@author: rudresh
"""

import pandas as pd
import numpy as np
#from pprint import pprint

customer = {
        "name":["Gopal","Ganesh","Mahadev","Gopal"],
        "age":[28,25,28,None],
        "contact":[4,9,16,25]
        }
customer_1 = {
        "name":["Manisha","Swati","Prachi","Lalita"],
        "age":[22,2,19,41],
        "contact":[123,3231,234,121]
        }
customer_2 = {
        "office":["Manisha","Swati","Prachi","Lalita"],
        "age":[22,21,19,1],
        "contact":[123,3231,234,121]
        }
df = pd.DataFrame(customer)
df_1 = pd.DataFrame(customer_1)
df_2 = pd.DataFrame(customer_2)
#print(df.iloc[:,0:1])
#print(pd.concat([df,pd.DataFrame({"name":["Ketaki"],"age":[24],"contact":[3332]})]).reset_index())
#print(df.sort_values('age',ascending=False).reset_index())
#print(pd.concat([df,df_1]).reset_index())
#print(df.melt().pivot(columns='variable', values='value'))
#print(pd.read_csv('demo.csv'))
#print(df[df["age"]>25])
#print(df[df.age>18].drop_duplicates('age'))
#print(df.nlargest(1,'age'))
#print(df.filter(regex='G$'))
#print(df['name'].value_counts())
#print(df['contact'].apply(np.sqrt))
#d = df.groupby(by='age')
#print(d.size())
#d = df.describe()
#print(d)
#print(df.dropna())
#df.plot.scatter(x="age",y="contact")
print(df_1*df_2)