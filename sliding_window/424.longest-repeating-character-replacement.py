#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (52.90%)
# Total Accepted:    590.9K
# Total Submissions: 1.1M
# Testcase Example:  '"ABAB"\n2'
#
# You are given a string s and an integer k. You can choose any character of
# the string and change it to any other uppercase English character. You can
# perform this operation at most k times.
# 
# Return the length of the longest substring containing the same letter you can
# get after performing the above operations.
# 
# 
# Example 1:
# 
# 
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# 
# 
# Example 2:
# 
# 
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length
# 
# 
#
# from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # TODO
        #fast solution

        # slow but intuitiive O(m*N) where m is up to 26 letters, N is len(s)
        letters = set(s)
        max_count = 0

        for l in letters:
            r_count=0
            i=0
            for j in range(len(s)):
                if s[j]!=l:
                    r_count+=1
                    if r_count > k:
                        while r_count > k:
                            if s[i]!=l:
                                r_count-=1
                            i+=1

                l_count = j-i+1
                max_count = max(max_count, l_count)

        return max_count
                
                    

            