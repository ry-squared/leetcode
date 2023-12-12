#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (62.86%)
# Total Accepted:    1.8M
# Total Submissions: 2.9M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# 
# 
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
# 
#
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # heap solution
        c = Counter(nums)
        k_top = heapq.nlargest(n=k, iterable=c.keys(), key=c.get)
        return k_top


        # less trivial, with list sort at end    
        # freq = defaultdict(lambda:0)
        # for num in nums:
        #     freq[num]+=1
            
        # freq = sorted(freq.items(), key=lambda x: x[1])
        # freq = [x[0] for x in freq[-k:]]

        # return freq
    

        # trivial
        # c = Counter(nums).most_common(k)
        # return [ci[0] for ci in c]