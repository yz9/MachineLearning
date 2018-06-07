#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
#plt.show()
################################################################################

# algorithm choices: 0. k nearest neighbors 1. adaboost (boosted decision tree)
alg_choice = 0
def getClassifier(choice):
    if choice == 0:
        print "k nearest neighbors"
        return KNeighborsClassifier(n_neighbors=5)
    elif choice == 1:
        print "Adaboost"
        return AdaBoostClassifier()
    return null

def processData(choice):
    clf = getClassifier(choice)
    # training
    clf.fit(features_train, labels_train)
    # prediction
    pred = clf.predict(features_test)
    print "accuracy score:", accuracy_score(labels_test,pred)
    prettyPicture(clf, features_test, labels_test)

try:
    processData(alg_choice)
except NameError:
    pass
