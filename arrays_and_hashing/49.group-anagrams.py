#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (67.19%)
# Total Accepted:    2.4M
# Total Submissions: 3.5M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
# 
# 
#
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_grouped = dict()
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted not in strs_grouped:
                strs_grouped[s_sorted]=[s]
            else:
                strs_grouped[s_sorted].append(s)

        return(list(strs_grouped.values()))