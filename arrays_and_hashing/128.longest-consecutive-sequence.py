#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (47.40%)
# Total Accepted:    1.5M
# Total Submissions: 3.1M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
# 
# You must write an algorithm that runs in O(n) time.
# 
# 
# Example 1:
# 
# 
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums)==0:
            return(0)

        nums = sorted(nums)
        counter=0
        max_counter=0
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] ==1:
                counter+=1
            elif nums[i+1]-nums[i] == 0:
                continue
            else:
                counter=0
            max_counter=max(counter, max_counter)
        return(max_counter+1)
