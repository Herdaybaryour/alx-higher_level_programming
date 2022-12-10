#!/usr/bin/python3
def roman_to_int(roman_string):

  numeral_values = {

    'I': 1,

    'V': 5,

    'X': 10,

    'L': 50,

    'C': 100,

    'D': 500,

    'M': 1000

  }


  result = 0

  for i in range(len(roman_string)-1, -1, -1):

    numeral = roman_string[i]
    value = numeral_values[numeral]

    if i == 0 or i == len(roman_string)-1 or numeral_values[roman_string[i-1]] <= value:

      result += value

    else:
      result -= value

  return result
