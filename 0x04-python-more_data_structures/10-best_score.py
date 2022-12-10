#!/usr/bin/python3
def get_max_key(a_dictionary):

  max_key = None

  max_value = None

  for key, value in a_dictionary.items():

    if isinstance(value, int):

      if max_value is None or value > max_value:

        max_key = key

        max_value = value

  return max_key
