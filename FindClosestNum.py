#Arrays
#Leetcode Qn no.2239

#Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

#Example 1:
#Input: nums = [-4,-2,1,4,8]
#Output: 1
#Explanation:
#The distance from -4 to 0 is |-4| = 4.
#The distance from -2 to 0 is |-2| = 2.
#The distance from 1 to 0 is |1| = 1.
#The distance from 4 to 0 is |4| = 4.
#The distance from 8 to 0 is |8| = 8.
#Thus, the closest number to 0 in the array is 1.

class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest = nums[0] #first element in the array
        for num in nums:
            if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):  #checking if num is smaller than already closest num or if they are equal
                closest = num 
        return closest

#time complexity - O(n)
