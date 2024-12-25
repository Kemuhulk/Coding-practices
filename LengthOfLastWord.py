# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words= s.strip().split()
        if words:
            return len(words[-1])  
        else:
            return 0

# Time Complexity: O(n)
