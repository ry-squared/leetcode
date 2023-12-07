#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (52.25%)
# Total Accepted:    2.8M
# Total Submissions: 5.3M
# Testcase Example:  '2'
#
# You are climbing a staircase. It takes n steps to reach the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# Example 2:
# 
# 
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 45
# 
# 
#

# exploit fibonacci sequence, each number of ways for n is sum of previous 2 num paths
class Solution:
    def climbStairs(self, n: int) -> int:

        i_curr = 0
        i_prev = 2
        i_prev_prev=1

        if n == 1:
            return(i_prev_prev)
        if n ==2:
            return(i_prev)

        for i in range(2, n):

            i_curr = i_prev + i_prev_prev
            i_prev_prev = i_prev
            i_prev = i_curr
        
        return(i_curr)
