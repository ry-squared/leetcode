#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (40.13%)
# Total Accepted:    2.4M
# Total Submissions: 6M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# There is an integer array nums sorted in ascending order (with distinct
# values).
# 
# Prior to being passed to your function, nums is possibly rotated at an
# unknown pivot index k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
# (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
# and become [4,5,6,7,0,1,2].
# 
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4
# 
# 
#
class Solution:

    def binary_search(self, nums, target, l, r):
        # normal binary search
        while l <= r:
            m=(l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l=m+1
            else:
                r=m-1
        return -1
    
    def leftmost_binary_pivot_search(self, nums):
        # find boundary, i.e. smallest num
        l=0
        r=len(nums)-1
        m=(l+r)//2
        while l < r:
            if nums[-1] < nums[m]:
                l=m+1
            else:
                r=m
            m=(l+r)//2
        return l

        
    def search(self, nums: List[int], target: int) -> int:
        
        pivot_idx = self.leftmost_binary_pivot_search(nums)
        l_result = self.binary_search(nums, target, l=0, r=pivot_idx)
        r_result = self.binary_search(nums, target, l=pivot_idx, r=len(nums)-1)

        result = max(l_result, r_result)

        return result