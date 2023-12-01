#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# https://leetcode.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (58.28%)
# Total Accepted:    1.2M
# Total Submissions: 2.1M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the root of a binary tree, return the length of the diameter of the
# tree.
# 
# The diameter of a binary tree is the length of the longest path between any
# two nodes in a tree. This path may or may not pass through the root.
# 
# The length of a path between two nodes is represented by the number of edges
# between them.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -100 <= Node.val <= 100
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
        self.max_dist = 0
        self.max_depth = 0

    def traverse_tree(self, root):
    
        if root!=None:
            l_depth = self.traverse_tree(root.left)
            r_depth = self.traverse_tree(root.right)

            if l_depth + r_depth > self.max_dist:
                self.max_dist = l_depth + r_depth

            self.max_depth = max(l_depth, r_depth) + 1
            
            return (self.max_depth)
        else:
            return 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        self.traverse_tree(root)
        return(self.max_dist)
        