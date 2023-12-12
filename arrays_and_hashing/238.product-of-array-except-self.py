#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (65.10%)
# Total Accepted:    2M
# Total Submissions: 3.1M
# Testcase Example:  '[1,2,3,4]'
#
# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].
# 
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
# 
# You must write an algorithm that runs in O(n) time and without using the
# division operation.
# 
# 
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
# 
# 
# 
# Follow up: Can you solve the problem in O(1) extra space complexity? (The
# output array does not count as extra space for space complexity analysis.)
# 
#
import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        products = []
        left_list = [1]
        right_list = [1]
        l=1
        r=1
        for i in range(len(nums)-1):
            l=l*nums[i]
            r=r*nums[-(i+1)]
            left_list.append(l)
            right_list.append(r)

        for i in range(len(nums)):
            products.append(left_list[i]*right_list[-(i+1)])

        return(products)


        # better
        # products = []
        # r = math.prod(nums[1:])
        # l = 1
        # for i in range(len(nums)-1):
        #     p=l*r
        #     products.append(p)

        #     l = l*nums[i]
        #     if nums[i+1] == 0:
        #         r = math.prod(nums[i+2:])
        #     else:
        #         r = r//nums[i+1]
        # products.append(l*r)
        # return(products)


        # trivial
        # products = []
        # total_prod = math.prod(nums)
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         p1 = math.prod(nums[0:i])
        #         p2 = math.prod(nums[i+1:])
        #         p = p1*p2
        #     else:
        #         p = total_prod//nums[i]
        #     products.append(p)

        # return products

        
