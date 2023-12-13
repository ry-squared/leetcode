#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (33.66%)
# Total Accepted:    3.1M
# Total Submissions: 9.3M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# 
# 
# Example 3:
# 
# 
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
# 
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
# 
# 
#
from collections import defaultdict
class Solution:
    def twoSum(self, nums, target=0):
        i=0
        j=len(nums)-1
        result = set()
        while i<j:
            lo=nums[i]
            hi=nums[j]
            if target + lo + hi == 0:
                r = target, lo, hi
                result.add(r)
            if target + lo + hi < 0:
                i+=1
            else:
                j-=1
        return(result)
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        result_total = set()
        num_prev = nums[0]-1
        for i in range(len(nums)):
            if nums[i]>0 or nums[i] == num_prev:
                num_prev=nums[i]
                continue
            else:
                num_prev=nums[i]
            result = self.twoSum(nums[i+1:], target=nums[i])
            if result:
                result_total.update(result)
        return(result_total)

            


