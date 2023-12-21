#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (65.90%)
# Total Accepted:    741.2K
# Total Submissions: 1.1M
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to
# wait after the i^th day to get a warmer temperature. If there is no future
# day for which this is possible, keep answer[i] == 0 instead.
# 
# 
# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
# 
# 
# Constraints:
# 
# 
# 1 <= temperatures.length <= 10^5
# 30 <= temperatures[i] <= 100
# 
# 
#
from math import inf
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        idxs_temps_stack = []

        offsets = [0]*len(temperatures)

        for i in range(len(temperatures)-1):

            current_idx = i
            next_idx = i+1

            current_temp = temperatures[current_idx]
            next_temp = temperatures[next_idx]

            # all idx, temps get added to stack
            idxs_temps_stack.append((current_idx, current_temp))

            while next_temp > current_temp:
                current_idx, _ = idxs_temps_stack.pop()
                offsets[current_idx] = next_idx - current_idx
                current_temp = (idxs_temps_stack[-1][1] if idxs_temps_stack else inf)

        return offsets