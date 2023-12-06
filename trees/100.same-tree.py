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

    def traverse_tree(self, p, q):

        if p!=None and q!=None:
            if p.val == q.val:
                l_match = self.traverse_tree(p.left, q.left)
                r_match = self.traverse_tree(p.right, q.right)
                return l_match and r_match
            else:
                return False

        elif p!=None and q==None:
            return False
        elif p==None and q!=None:
            return False
        elif p==None and q==None:
            return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        return(self.traverse_tree(p,q))