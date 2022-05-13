# -*- coding: utf-8 -*-
"""
Created on Fri May 13 22:19:19 2022

@author: Yasser Ezzat
"""
import pandas as pd

import seaborn as sns
df=pd.read_excel('data/images_analyzed.xlsx')

# sns.lmplot(x="Time",y="Images_Analyzed",data=df,hue="Age",order=2)
# sns.lmplot(x="Coffee",y="Images_Analyzed",data=df,hue="Age",order=2)

from sklearn.linear_model import LinearRegression

#create instance of model

reg=LinearRegression()

reg.fit(df[['Time','Coffee','Age']],df[['Images_Analyzed']])
print(reg.coef_)
print(reg.predict([[13,2,23]]))





