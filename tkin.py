#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 08:40:36 2019

@author: rudresh
"""
from tkinter import *
root = Tk()

l = Label(root,text="ID")
nid = Entry(root)
l1 = Label(root,text="Name")
name = Entry(root)
insert = Button(root, text="Insert")
update = Button(root, text="Update")
delete = Button(root, text="Delete")
view = Button(root, text="View")
for w in (l,nid, l1, name, insert,update,delete,view):
    w.pack()
root.mainloop()