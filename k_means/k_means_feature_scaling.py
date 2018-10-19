# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 22:10:34 2017

@author: JasonMedina
"""

import pickle
import numpy
from sklearn.preprocessing import MinMaxScaler
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)


feature_1 = "salary"
feature_2 = "exercised_stock_options"
poi  = "poi"

features_list = [poi, feature_1, feature_2 ]
data_dict = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data_dict )

# Set two lists for salary, and Stock, add the original value at the [0] position
salary = [[200000.]]
stock =[[1000000.]]

for f1, f2 in finance_features:
    salary.append([f1])
    stock.append([f2])

# MinMaxScaler
stock =numpy.array(stock)
scaler = MinMaxScaler()
rescaled_stock= scaler.fit_transform(stock)

salary =numpy.array(salary)
scaler = MinMaxScaler()
rescaled_salary= scaler.fit_transform(salary)

print rescaled_salary[0]
print rescaled_stock[0]