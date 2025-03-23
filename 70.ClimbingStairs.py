# Leetcode qn.70 Dynamic Programming 

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 1
        if n==2: return 2
        one_back = 2
        two_back = 1
        for i in range(3, n+1):
            curr = one_back + two_back
            two_back = one_back
            one_back = curr
        return curr
