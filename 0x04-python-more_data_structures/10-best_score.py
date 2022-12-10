#!/bin/python3

def best_score(a_dict):

    if a_dict is None or a_dict == {}:

        return None

    biggest = max(a_dict.values())

    for key, value in a_dict.items():

        if value is biggest:

            return key
