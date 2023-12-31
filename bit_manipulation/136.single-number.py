#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (71.85%)
# Total Accepted:    2.5M
# Total Submissions: 3.4M
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one.
# 
# You must implement a solution with a linear runtime complexity and use only
# constant extra space.
# 
# 
# Example 1:
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:
# Input: nums = [1]
# Output: 1
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
# Each element in the array appears twice except for one element which appears
# only once.
# 
# 
#
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        nums = sorted(nums)

        if len(nums)==1:
            return(nums[0])

        if nums[0]!=nums[1]:
            return(nums[0])

        for i in range(1, len(nums)-1):
            num_next = nums[i+1]
            num_current = nums[i]
            num_prev = nums[i-1]
            if num_next!=num_current and num_current!=num_prev:
                return num_current
            
        return num_next
        
