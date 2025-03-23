#Array

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
# Example:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                prev_empty = ( i==0 or flowerbed[i-1] == 0 )
                next_empty = ( i == length - 1 or flowerbed[i+1] == 0)
                if prev_empty and next_empty:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        return count >= n
