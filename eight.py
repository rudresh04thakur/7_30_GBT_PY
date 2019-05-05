#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 09:12:07 2019

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
class Bank:
    def calculate(self,s):
            temp = s.split(" ")
            if(temp[0]=="D"):
                global deposit
                deposit += int(temp[1])
            elif(temp[0]=="W"):
                global withdrawl
                withdrawl += int(temp[1])
    def getInput(self):
        d=dict({})
        n = int(input("Enter Number of Transactions : "))
        for i in range(0,n):
            s = (input("Enter Transaction with prefix D(deposit)/W(Withdrawl)").split(" "))
            for j in range(0,len(s)-1,2):
                d[s[j]]= s[j+1] 
        print(d)
    #calculate(input("Enter Transaction with prefix D(deposit)/W(Withdrawl)"))


if __name__=='__main__':
    b = Bank()
    print(b.getInput())
    print(deposit,withdrawl)




