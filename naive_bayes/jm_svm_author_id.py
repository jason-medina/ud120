# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 16:07:39 2017

@author: JasonMedina
"""

#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
import os
from time import time
#os.chdir('C:\\Users\\JasonMedina\\Downloads\\ud120-projects-master\\ud120-projects-master\\naive_bayes')
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#########################################################
from sklearn.svm import SVC
clf = SVC(kernel="linear")


clf.fit(features_train,labels_train)

SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel='linear', max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
  
clf.score(features_test,labels_test)