#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 18:21:34 2019

@author: rudresh
"""

'''
    variable

'''

data_number = 21
data_string = "Ganesh"
data_boolean = True
data_list = ["Ganesh","Nanded",27]
data_dict = {"name":"Gopal","city":"Nanded","age":27}
data_tuple = ("python",)
data_set = { "Gopal","Gopal","Ganesh","Mahesh" }
print(data_number,data_string,data_boolean,data_list,data_dict,data_tuple,data_set)

'''
Operators 
1) Math : + - / * ** // %
2) Conditional > < == >= <= 
3) Assingment =
4) Bitwise & | >> << ! ^
5) Logical and or not 

'''
'''
 Branching Statements    
'''
 
if(data_number == 20):
    print("data is 20")
else:
    if(data_number<10):
        print("data is less than 10")
    elif(data_number >20):
        print("data is greter than 20")
    else:
        print("data is 10")
        
for i in data_list:
    print(i)
    
for j in range(0,10,2):
    print(j)
    
def add(a,b):
    print(a+b)
add(20,18)

x = lambda a,b : a-b
print(x(12,6))

class Employee:
   def __init__(self):
       self.name = None
   def printInfo(self,name):
       self.name = name
       print("Name is %s" % (self.name))

class Account(Employee):
   def __init__(self):
       self.bank_name = None
   def printInfo_A(self,bank_name):
       self.bank_name = bank_name
       print("Name is %s" % (self.bank_name))
       
e = Account()
e.printInfo("Vedika")
e.printInfo_A("Union Bank")

import pandas as pd

# DataFreame
# Seriese
l = {"name":["Gopal","Ganesh","Mahesh"],"age":[28,28,28],"contact":[123,232,22]}
df = pd.DataFrame(l)
#print(df.melt())
j = pd.DataFrame(df.melt().pivot(columns="variable",values="value"))

l_1 = {"name":["Gopal","Ganesh","Mahesh"],"age":[28,23,43],"contact":[123,232,321]}
df_1 = pd.DataFrame(l_1)

#print(pd.concat([df,df_1]).drop_duplicates())

#print(df.head(1))  //recheck

#print(df.nsmallest(2,columns=['age']))
#print(df.sort_values('age',ascending=False))
#print(df.rename(columns={'age':'old','contact':'mobile'}))
#print(df.drop(columns=['age']))
#print(df[['name','age']])
#print(df.loc[:,'age'])
#print(df.assign(Area=lambda df: df.age*df.contact))

#print(pd.qcut(df.age, 1)) //recheck


#print(df.groupby('age').count())
#print(df.plot.hist())
print(df.plot.scatter(x='age',y='contact'))





