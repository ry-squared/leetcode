#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (46.19%)
# Total Accepted:    732.1K
# Total Submissions: 1.6M
# Testcase Example:  '[1,5,11,5]'
#
# Given an integer array nums, return true if you can partition the array into
# two subsets such that the sum of the elements in both subsets is equal or
# false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
# 
# 
#
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
