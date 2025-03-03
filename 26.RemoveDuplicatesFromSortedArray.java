// Leetcode question no.26 : Remove Duplicates From Sorted Array
  
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;

        int i=0;  // Pointer for unique elements
        for(int j=1;j<nums.length;j++){
            if(nums[j]!=nums[i]){  // Found a new unique element
                i++;
                nums[i]=nums[j];  // Move unique element to its position
            }
        }
        return i+1;  // Unique count
    }
}
