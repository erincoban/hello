# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 13:27:13 2023

@author: ERİN
"""

import numpy as np

i = 0.03
M = 100
C = 5

N = np.arange(1, 11)  # Maturities between 1 and 10 (inclusive)

bond_prices = C * (1 - (1 + i)**(-N)) / i + M * (1 + i)**(-N)

print(bond_prices)


#Below, we will create an array that contains 10 points between 0 and 25.

# This is similar to range -- but spits out 10 evenly spaced points from 0.5 to 25.
x = np.linspace(0.5, 25, 10)
#We will experiment with some ufuncs below:
print(x)

# Applies the sin function to each element of x
np.sin(x)
#You can use the inspector or the docstrings with np.<TAB> to see other available functions, such as
print(np.sin(x))
# Takes natural log of each element of x
print(np.log(x))
