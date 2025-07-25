#roman to integer conversion
class Solution:   
    def roman_to_int(self, s: str ) ->  int:

      roman = {
          'I': 1,
          'V': 5,
          'X': 10,
          'L': 50,
          'C': 100,
          'D': 500,
          'M': 1000
      }
      res = 0
      prev_value = 0
      for char in reversed(s):
          curr_value = roman[char]
          if curr_value < prev_value:
              res -= curr_value
          else:
              res += curr_value
          prev_value = curr_value
      return res
