# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 22:34:19 2022

@author: Efrain
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functools import partialmethod
from sklearn import  preprocessing

# x = np.random.normal(170, 10, 250)

# plt.hist(x)
# plt.show() 


contenido = pd.read_csv("sleepdatadep.csv")
#print(contenido)
#contenido.head(10)
contenido['Heart rate'] = contenido['Heart rate'].fillna(contenido['Heart rate'].mean())
y = contenido.pop("QUALITY SLEEP")
z = contenido.pop("Cafeine")
#contenido['Heart rate'] = contenido['Heart rate'].fillna(contenido['Heart rate'].mean())

plt.hist(z)
plt.show() 