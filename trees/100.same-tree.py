#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (60.06%)
# Total Accepted:    1.8M
# Total Submissions: 3M
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given the roots of two binary trees p and q, write a function to check if
# they are the same or not.
# 
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.
# 
# 
# Example 1:
# 
# 
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: p = [1,2], q = [1,null,2]
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in both trees is in the range [0, 100].
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
        self.is_same=True

    def traverse_tree(self, p, q):
        
        if p and q:
            if p.val != q.val:
                self.is_same = False
            self.traverse_tree(p.left, q.left)
            self.traverse_tree(p.right, q.right)
                
        if (p and not q) or (q and not p):
            self.is_same = False

        return(self.is_same)        
        

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        return(self.traverse_tree(p,q))