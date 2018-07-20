#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn import cross_validation
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### randomly split into training and test sets
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(
    features, labels, test_size=0.3, random_state=42)

### create decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print "accuracy score:", accuracy_score(labels_test, pred)

positive_poi = [poi for poi in pred if poi==1]
positive_poi_size = len(positive_poi)
test_size = len(features_test)
print "predicted POTs:", positive_poi_size
print "total number in test set", test_size
print "accuracy for negative poi predicted %0.3f" % (float(test_size-positive_poi_size)/test_size)

def calculateTerms(labels_test, pred):
    true_positive = false_negative = false_positive = true_negative = 0;
    print "===================="
    for actual_label, predict in zip(labels_test, pred):
        if actual_label == 1 and predict == 1:
            true_positive += 1
        elif actual_label == 1 and predict == 0:
            false_negative += 1
        elif actual_label == 0 and predict == 1:
            false_positive += 1
        elif actual_label == 0 and predict == 0:
            true_negative += 1
    print "total number of true positives", true_positive
    print "total number of true negatives", true_negative
    print "total number of false positives", false_positive
    print "total number of false negatives", false_negative
    print "precision %0.3f" % (float(true_positive)/(true_positive+false_positive))
    print "recall %0.3f" % (float(true_positive)/(true_positive+false_negative))
    print "===================="

calculateTerms(labels_test, pred)

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

calculateTerms(true_labels, predictions)
