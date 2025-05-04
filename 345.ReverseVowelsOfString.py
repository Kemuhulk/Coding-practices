# Two pointers #String 
# Leetcode 75 4th qn
# Leetcode qn.no.345 

# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation: The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        s = list(s)
        left, right = 0, len(s)-1
        
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)
        
