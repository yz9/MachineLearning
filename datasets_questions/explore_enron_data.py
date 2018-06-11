#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here"s an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print "number of data points:", len(enron_data)
print "number of features available:", len(enron_data[enron_data.keys()[0]])

poi_counter = 0;
for name in enron_data:
    features = enron_data[name]
    if features["poi"]:
        poi_counter += 1
print "number of POIs in E+F dataset:", poi_counter

print "total value of the stock belonging to James Prentice:", enron_data["PRENTICE JAMES"]["total_stock_value"]
print "number of email messages from Wesley Colwell to POI:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "value of stock options by Jeffrey K Skilling:", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

enrol_payments = {}
enrol_payments["FASTOW ANDREW S"] = enron_data["FASTOW ANDREW S"]["total_payments"]
enrol_payments["LAY KENNETH L"] = enron_data["LAY KENNETH L"]["total_payments"]
enrol_payments["SKILLING JEFFREY K"] = enron_data["SKILLING JEFFREY K"]["total_payments"]

max_key = max(enrol_payments, key=enrol_payments.get)
print "%s took the most money %d" % (max_key, enrol_payments[max_key])

print "total payemnts of Fastow", enron_data["FASTOW ANDREW S"]["total_payments"]
print "total payemnts of Lay", enron_data["LAY KENNETH L"]["total_payments"]
print "total payemnts of Skilling", enron_data["SKILLING JEFFREY K"]["total_payments"]

num_salary = num_email = num_payments = num_nan_payments = num_nan_poi_payments= 0
for name in enron_data:
    features = enron_data[name]
    if features["salary"] != "NaN":
        num_salary += 1
    if features["email_address"] != "NaN":
        num_email += 1
    if features["total_payments"] == "NaN":
        num_nan_payments += 1
        if features["poi"]:
            num_nan_poi_payments +=1

print num_nan_poi_payments
print poi_counter
print "number of folks having quantified salary:", num_salary
print "number of folks having quantified email:", num_email
print "percentage of people having \"NaN\" as for their total payments:", float(num_nan_payments)/len(enron_data) * 100
print "percentage of POIs people having \"NaN\" as for their total payments:", float(num_nan_poi_payments)/poi_counter * 100
