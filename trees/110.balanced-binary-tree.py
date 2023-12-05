#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (50.83%)
# Total Accepted:    1.3M
# Total Submissions: 2.6M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: root = []
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 5000].
# -10^4 <= Node.val <= 10^4
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.balanced = True

    def traverse_tree(self, root, max_depth=0):
       
        
       if root!=None and self.balanced==True:
            max_depth+=1
            l_depth = self.traverse_tree(root.left, max_depth)
            r_depth = self.traverse_tree(root.right, max_depth)
            dist_diff = abs(l_depth - r_depth)
            if dist_diff > 1:
                self.balanced=False
            max_depth = max(l_depth, r_depth)
            return max_depth
       else:
            return(max_depth)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.traverse_tree(root)

        return(self.balanced)
        

        
