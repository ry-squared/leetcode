#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (74.71%)
# Total Accepted:    2.7M
# Total Submissions: 3.6M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return its maximum depth.
# 
# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: root = [1,null,2]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
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
    # def maxDepth(self, root: Optional[TreeNode]) -> int:

    #     current_depth = 0
    #     # DFS
    #     def traverse_tree(root, current_depth):

    #         if root!= None:
    #             current_depth+=1
    #             l_depth = traverse_tree(root.left,  current_depth)
    #             r_depth = traverse_tree(root.right,  current_depth)
    #             return(max(l_depth, r_depth))

    #         return(current_depth)
            
            
    #     return(traverse_tree(root, current_depth))
    


    # def __init__(self):
    #     self.max_depth= 0
    
    # max_depth is local variable within each funciton call
    def traverse_tree(self, root, max_depth=0):
        
       if root != None:
            max_depth+=1
            l_depth = self.traverse_tree(root.left, max_depth)
            r_depth = self.traverse_tree(root.right, max_depth)
            max_depth = max(l_depth, r_depth)
            return max_depth
       
       else:
           return(max_depth)
       
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        self.traverse_tree(root)

        return(self.traverse_tree(root))


        
