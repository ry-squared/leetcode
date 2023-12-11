#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Easy (77.70%)
# Total Accepted:    983.1K
# Total Submissions: 1.3M
# Testcase Example:  '2'
#
# Given an integer n, return an array ans of length n + 1 such that for each i
# (0 <= i <= n), ans[i] is the number of 1's in the binary representation of
# i.
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 
# 
# Example 2:
# 
# 
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 10^5
# 
# 
# 
# Follow up:
# 
# 
# It is very easy to come up with a solution with a runtime of O(n log n). Can
# you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like
# __builtin_popcount in C++)?
# 
# 
#
class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # dynamic programming
        bit_counts = list(range(n+1))
        bit_counts[0]=0
        for i in range(1,n+1):
            bit_counts[i]=bit_counts[i&(i-1)]+1
        return bit_counts


        # counting for each i in N using efficient counting
        # def count_bits(n):
        #     count_bits = 0
        #     while n !=0:
        #         n=n&(n-1) #pop least significant 1 bit until all 0s
        #         count_bits+=1
        #     return(count_bits)
        

        # bit_counts = []
        # for i in range(n+1):
        #     bit_counts.append(count_bits(i))
        # return(bit_counts)
            
        # trivial solution
        # bit_counts = []
        # for i in range(n+1):
        #     bit_counts.append(i.bit_count())

        # return bit_counts
        
