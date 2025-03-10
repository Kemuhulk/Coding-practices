# Tree
# Leetcode qn.98 Validate Binary Search Tree

# Example 1:
#   2
#  / \
# 1   3
# Input: root = [2,1,3]
# Output: true

# Example 2:
#   5
#  / \
# 1   4
#    / \
#   3   6
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def is_bst(node, left_bound, right_bound):
            if not node:
                return True
            if not (left_bound < node.val < right_bound):
                return False
            return (is_bst(node.left, left_bound, node.val) and is_bst(node.right, node.val, right_bound))
        return is_bst(root, float("-inf"), float("inf"))
