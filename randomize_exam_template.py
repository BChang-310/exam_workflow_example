# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:08:08 2021

@author: bchan
"""

import numpy as np
import sys
# np.random.seed(0)

f = open("example_exam.ipynb", 'r')

a = f.read()
f.close()

a_number = np.random.randint(20, size=3)


a = a.replace("a21 & a22 & a23", 
              f"{a_number[0]} & {a_number[1]} & {a_number[2]}")

output_file = open('example_exam.ipynb', 'w')
output_file.write(a)
output_file.close()
