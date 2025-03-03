##Fibonacci Number

# Leetcode qn.no.509

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr=[0,1]
        for i in range(2, n+1):
            arr.append(arr[i-1]+arr[i-2])
        return arr[n]
