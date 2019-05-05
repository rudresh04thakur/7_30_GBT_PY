#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 08:36:20 2019

@author: rudresh
"""

import numpy as np
z = np.array([[2,3,4],[11,22,33]])
#print(z.reshape((3,3),order='C'))
#np.savetxt('array.txt',z)
print(z)
print(z.transpose())
