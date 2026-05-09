#Arrays
#Leetcode qn.no 1431

# Example:1
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 

# Example:2
# Input: candies = [4,2,1,1,2], extraCandies = 1
# Output: [true,false,false,false,false]

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = candies[0]

        for candy in candies:
            if candy > max_candies:
                max_candies = candy
        
        result = []

        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
                
        return result
