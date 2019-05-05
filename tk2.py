#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 08:51:51 2019

@author: rudresh
"""

from tkinter import *
#from PIL import ImageTk, Image
tkmain = Tk()
tkmain.title("Registration")

root = Frame(tkmain, bg='cyan', width = 500, height=250, pady=3,padx=3).grid(row=0, columnspan=4,rowspan=5)

labelId = Label(root,text="ID").grid(row=0,column=0,sticky=W)
entryId = Entry(root).grid(row=0,column=1,sticky=W)

labelName = Label(root,text="Name").grid(row=1,column=0,sticky=W)
entryName = Entry(root).grid(row=1,column=1,sticky=W)

labelDob = Label(root,text="DOB").grid(row=2,column=0,sticky=W)
entryDob = Entry(root).grid(row=2,column=1,sticky=W)

labelGender = Label(root,text="Gender").grid(row=3,column=0,sticky=W)
v = IntVar()
maleRadio=Radiobutton(root, text="Male", variable=v, value=1).grid(row=3,column=1,sticky=W)
femaleRadio=Radiobutton(root, text="Female", variable=v, value=2).grid(row=3,column=2,sticky=W)

labelBloodGroup = Label(root,text="Blood Group").grid(row=4,column=0,sticky=W)
variableBG = StringVar(root)
variableBG.set("O+") # default value
entryBloodGroup = OptionMenu(root, variableBG, "O+", "A+", "B+","AB+","O-", "A-", "B-","AB-").grid(row=4,column=1,sticky=W)

#img = ImageTk.PhotoImage(Image.open("BackUp/DR-avatar.png"))
label = Label(root,height=100,width=100)
label.grid(row=4,column=2,sticky=W)
#label.image = img # keep a reference!

tk = Frame(tkmain, bg='Blue', width = 500, height=250, pady=3,padx=3).grid(row=5, columnspan=4,rowspan=5)
labelAddress = Label(tk,text="Address").grid(row=5,column=0,sticky=W)
entryAddress = Text(tk,height=2,width=15).grid(row=5,column=1,sticky=W)

labelCity = Label(tk,text="City").grid(row=6,column=0,sticky=W)
variableCity = StringVar(tk)
variableCity.set("Pune") # default value
entryCity = OptionMenu(tk, variableCity, "Pune", "Nashik", "Nanded","Hydrabad","Jalna", "Sangli", "Satara","Aurangabad").grid(row=6,column=1,sticky=W)

labelMobile = Label(tk,text="Mobile Number").grid(row=7,column=0,sticky=W)
entryMobile = Entry(tk).grid(row=7,column=1,sticky=W)

labelEmail = Label(tk,text="Email").grid(row=8,column=0,sticky=W)
entryEmail = Entry(tk).grid(row=8,column=1,sticky=W,pady=5)


insert = Button(tk, text="Insert").grid(row=9,column=0,sticky=W)
update = Button(tk, text="Update").grid(row=9,column=1,sticky=W)
delete = Button(tk, text="Delete").grid(row=9,column=2,sticky=W)
view = Button(tk, text="View").grid(row=9,column=3,sticky=E)

tkmain.mainloop()