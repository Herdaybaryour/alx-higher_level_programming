def roman_to_int(roman_string):

  # define a dictionary with the values of each Roman numeral

  numeral_values = {

    'I': 1,

    'V': 5,

    'X': 10,

    'L': 50,

    'C': 100,

    'D': 500,

    'M': 1000

  }



  # initialize the result to 0

  result = 0



  # iterate over the Roman numeral string in reverse

  for i in range(len(roman_string)-1, -1, -1):

    # get the current numeral and its value

    numeral = roman_string[i]

    value = numeral_values[numeral]



    # if the numeral is the first or the last in the string

    # or if the numeral to the right has a lower value,

    # add the value to the result

    if i == 0 or i == len(roman_string)-1 or numeral_values[roman_string[i-1]] <= value:

      result += value

    # otherwise, subtract the value from the result

    else:

      result -= value



  return result

