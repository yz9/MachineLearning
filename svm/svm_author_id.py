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
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# slice the training dataset to train just 1% of the full training set
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

"""
    training time: 257.226s
    prediction time: 29.913s
    accuracy score: 0.984072810011

    -After slice the training dataset:
    traning time: 0.15s
    prediction time: 1.671
    accuracy score:
    linear kernel: 0.88
    rbf kernel: 0.61
"""
# svm classifier
clf = SVC(kernel='rbf', C=10000.0)
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"
print "accuracy score:", accuracy_score(labels_test,pred)

count = 0
for p in pred:
    if p == 1:
        count += 1
print "total number of prediction(author Chris)", count
