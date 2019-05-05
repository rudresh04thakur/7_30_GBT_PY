#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 08:18:22 2019

@author: rudresh

input: 
    D 0200
    D 0300
    W 4000
    D 4000
    W 0234
output 
    D 4500
    W 4234
"""
deposit = 0
withdrawl = 0
def calculate(s):
    #deposit = 0
    #withdrawl = 0
    #for i in s:
        #temp = i.split(" ")
        temp = s.split(" ")
        if(temp[0]=="D"):
            global deposit
            deposit += int(temp[1])
        elif(temp[0]=="W"):
            global withdrawl
            withdrawl += int(temp[1])
    #return {"Deposit": deposit, "Withdrawl": withdrawl}

def getInput():
    n = int(input("Enter Number of Transactions : "))
    #s=list([])
    for i in range(0,n):
        #s.append(input("Enter Transaction with prefix D(deposit)/W(Withdrawl)"))
        calculate(input("Enter Transaction with prefix D(deposit)/W(Withdrawl)"))
    #return s



if __name__=='__main__':
    #print(calculate(getInput()))
    print(getInput())
    print(deposit,withdrawl)





