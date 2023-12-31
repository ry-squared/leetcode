#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (47.21%)
# Total Accepted:    754.4K
# Total Submissions: 1.6M
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# Given the roots of two binary trees root and subRoot, return true if there is
# a subtree of root with the same structure and node values of subRoot and
# false otherwise.
# 
# A subtree of a binary tree tree is a tree that consists of a node in tree and
# all of this node's descendants. The tree tree could also be considered as a
# subtree of itself.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -10^4 <= root.val <= 10^4
# -10^4 <= subRoot.val <= 10^4
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

    def sameTree(self, p, q):

        if (p and q is None) or (p is None and q):
            return False
        
        if not p and not q:
            return True

        if p and q:
            if p.val != q.val:
                return False
            else:
                l_match = self.sameTree(p.left, q.left)
                r_match = self.sameTree(p.right, q.right)
                return l_match and r_match    
            
    def traverse_tree(self, root, subTree):
        
        trees_match = self.sameTree(root, subTree)

        if trees_match:
            return True
        else:
            if root:
                l_match = self.traverse_tree(root.left, subTree)
                r_match = self.traverse_tree(root.right, subTree)
                return l_match or r_match
            else:
                return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subtree_match = self.traverse_tree(root, subRoot)
        return(subtree_match)
    

