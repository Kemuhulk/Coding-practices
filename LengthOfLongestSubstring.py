## Sliding window problem

# Leetcode Question no.3

# Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

 class Solution(object):
  def lengthOfLongestSubstring(self, s):
      """
      :type s: str
      :rtype: int
      """
      i=0
      longest = 0
      nset = set()
      n = len(s)
      
      for j in range(n):
          while s[j] in nset:
              nset.remove(s[i])
              i += 1
          w = (j - i) + 1 #window size
          if (longest > w):
              longest = longest
          else:
              longest = w
          nset.add(s[j])
      return longest        
