#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    #cleaned_data = []
    # construct a data list with age, net_worth in place plus one extra param for square error
    data = [(age, net_worth, pred - net_worth) for age, net_worth, pred in zip (ages, net_worths, predictions)]
    sorted_data = sorted(data,key=lambda tup:tup[2])
    # Clean away the 10% of points with largest residual errors
    cleaned_data = sorted_data[:-9]

    return cleaned_data
