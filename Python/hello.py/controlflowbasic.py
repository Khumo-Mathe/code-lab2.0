#roman to integer conversion
import re


class Solution:

    def roman_to_int(self, s: str) -> int:

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
      
      for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
      return res

s = input("Enter a Roman numeral: ")
solution = Solution()
print(solution.roman_to_int(s))