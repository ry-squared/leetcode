#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
# https://leetcode.com/problems/koko-eating-bananas/description/
#
# algorithms
# Medium (49.51%)
# Total Accepted:    496.9K
# Total Submissions: 1M
# Testcase Example:  '[3,6,7,11]\n8'
#
# Koko loves to eat bananas. There are n piles of bananas, the i^th pile has
# piles[i] bananas. The guards have gone and will come back in h hours.
# 
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she
# chooses some pile of bananas and eats k bananas from that pile. If the pile
# has less than k bananas, she eats all of them instead and will not eat any
# more bananas during this hour.
# 
# Koko likes to eat slowly but still wants to finish eating all the bananas
# before the guards return.
# 
# Return the minimum integer k such that she can eat all the bananas within h
# hours.
# 
# 
# Example 1:
# 
# 
# Input: piles = [3,6,7,11], h = 8
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# 
# 
# Example 3:
# 
# 
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
# 
# 
# 
# Constraints:
# 
# 
# 1 <= piles.length <= 10^4
# piles.length <= h <= 10^9
# 1 <= piles[i] <= 10^9
# 
# 
#
import math
class Solution:

    def calculate_hours(self, k, piles):
        return sum([math.ceil(p/k) for p in piles])

    def leftmost_descending_binary_search(self, target, piles):
        # abstract array with idxs that represent k
        # values of array represent hours of banana eating
        # e.g. piles = [3,6,7,11] and h=8
        # idxs k and hours from calculate_hours function
        # k = [1,  2,  3,  4, 5, 6, 7, 8, 9, 10, 11]
        # h = [27, 15, 10, 8, 8, 6, 5, 5, 5,  5,  4]
        #i=0,l=1,r=11,m=6,mid_num=6 <= target
        #i=1,l=1,r=6,m=3,mid_num=10 > target
        #i=2,l=4,r=6,m=5,mid_num=8 <= target
        #i=3,l=4,r=5,m=4,mid_num=8 <= target
        # r-> 4 and fin
        # leftmost k, i.e. smallest k where target matches is k=4,h=8
        l=1
        r=max(piles)
        m=(l+r)//2
        
        while l<r:

            mid_num = self.calculate_hours(m, piles)

            if mid_num > target:
                l=m+1
            elif mid_num <= target:
                r=m

            m=(l+r)//2

        return l

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        return self.leftmost_descending_binary_search(target=h, piles=piles)