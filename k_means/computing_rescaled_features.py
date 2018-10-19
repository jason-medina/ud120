# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 22:24:13 2017

@author: JasonMedina
"""
import pickle
from feature_format import featureFormat, targetFeatureSplit
import numpy

data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

feature_1 = "salary"
feature_2 = "exercised_stock_options"
poi  = "poi"

features_list = [poi, feature_1, feature_2 ]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )

# Set two lists for salary, and Stock, add the original value at the [0] position
salary = [[200000.]]
stock =[[1000000.]]

for f1, f2 in finance_features:
    salary.append([f1])
    stock.append([f2])

# MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
stock =numpy.array(stock)
scaler = MinMaxScaler()
rescaled_finance_features = scaler.fit_transform(finance_features)
rescaled_stock= scaler.fit_transform(stock)

#financial_features_test = numpy.array([200000., 1000000.])
#financial_features_test_transformed = scaler.transform(financial_features_test)
#print financial_features_test_transformed

salary =numpy.array(salary)
scaler = MinMaxScaler()
rescaled_salary= scaler.fit_transform(salary)

print rescaled_salary[0]
print rescaled_stock[0]