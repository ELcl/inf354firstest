# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 21:39:44 2022

@author: Efrain
"""
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
prepo = SimpleImputer(missing_values=np.nan, strategy="mean")
prepo1 = SimpleImputer(missing_values=np.nan, strategy="most_frequent")
X1=np.array([
                [1     ,2     ,3],
                [4     ,np.nan,5],
                [np.nan,1     ,np.nan]
             ])
X2 = prepo.fit_transform(X1)
contenido = pd.read_csv("sleep.csv")
X3 = prepo1.fit_transform(contenido)
print(X3)

