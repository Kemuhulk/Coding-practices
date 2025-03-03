# String
# Leetcode qn.no 1071

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

class Solution(object):
    
    def find_gcd(self, a, b):
        while b:
          # Keep reducing until remainder is 0
            a, b = b, a%b   # Apply Euclidean algorithm
        return a

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # If concatenating in different orders gives different results, return ""
        if str1 + str2! = str2 + str1:
            return ""
          
        # GCD of str1 and str2
        gcd_length = self.find_gcd(len(str1), len(str2))
      
        # The common divisor string will be the prefix of str1 of length gcd_length
        return str1[:gcd_length]


        
