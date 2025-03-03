# Input: nums = [3,2,4], target = 6
# Output: [1,2]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numtoindex = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in numtoindex:
                return (numtoindex[complement],index)
            numtoindex[num]=index

#Time complexity: O(n)
#Space complexity: O(n)     
