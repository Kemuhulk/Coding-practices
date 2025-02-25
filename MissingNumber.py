# Leetcode qn.no.268 Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:
# Input: nums = [3,0,1]
# Output: 2

# Example 2:
# Input: nums = [0,1]
# Output: 2

#method 1:
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for index,val in enumerate(nums): #enumerate adds a counter to an iterable
            if index!=val:
                return index
            if val == len(nums)-1:
                return val+1
#time complexity:O(NlogN)

#method 2:
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums)+1)) - sum(nums)
#time complexity:O(N)
