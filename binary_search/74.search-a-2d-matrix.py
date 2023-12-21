#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (49.42%)
# Total Accepted:    1.5M
# Total Submissions: 3.1M
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# You are given an m x n integer matrix matrix with the following two
# properties:
# 
# 
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the
# previous row.
# 
# 
# Given an integer target, return true if target is in matrix or false
# otherwise.
# 
# You must write a solution in O(log(m * n)) time complexity.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
# 
# 
#
class Solution:

    def binary_search(self, nums, target):
        l = 0
        r = len(nums)-1
        m = (r+l)//2

        while l <= r:
            mid_num = nums[m]
            if mid_num == target:
                return True
            elif target > mid_num:
                l=m+1
            else:
                r=m-1
            m = (r+l)//2

        return False
    
    def binary_matrix_search(self, rows, target):
        l = 0
        r = len(rows)-1
        m = (r+l)//2

        while l <= r:
            mid_row = rows[m]
            lo_num = rows[m][0]
            hi_num = rows[m][-1]
            if lo_num<=target<=hi_num:
                return mid_row
            elif target > hi_num:
                l=m+1
            else:
                r=m-1
            m = (r+l)//2

        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # double binary search
        res = self.binary_matrix_search(matrix, target)
        if res:
            res = self.binary_search(res, target)
        return res


        ## intuitive but slightly slower
        # res = False
        # for row in matrix:
        #     lo = row[0]
        #     hi = row[-1]

        #     if lo <= target <= hi:
        #         res = self.binary_search(row, target)
        #         return res

        # return res