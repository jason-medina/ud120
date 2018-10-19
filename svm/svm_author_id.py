#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
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

#timing codes around fit models
t0 = time()
clf.fit(features_train,labels_train)
print "training time on entire dataset:", round(time()-t0, 3), "s"

SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel='linear', max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)

#timing codes around prediction models
t0 = time()  
accuracyTest = clf.score(features_test,labels_test)
print "SVM model accuracy on entire dataset:", accuracyTest
print "prediction time on entire dataset:", round(time()-t0, 3), "s"

#speed up algorithim by training on smaller dataset
features_train1Pct = features_train[:len(features_train)/100]
labels_train1Pct = labels_train[:len(labels_train)/100]

#timing codes around fit
t0 = time()
clf.fit(features_train1Pct,labels_train1Pct)
print "training time on 1% dataset:", round(time()-t0, 3), "s"

#set kernel to rbf
SVC(C=10000, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel='rbf', max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
 
#timing codes around prediction
t0 = time()
accuracyTrain = clf.score(features_train1Pct,labels_train1Pct)
print "SVM model accuracy on 1% dataset:", accuracyTrain
print "prediction time on 1% dataset:", round(time()-t0, 3), "s"

#0.88452787258248011