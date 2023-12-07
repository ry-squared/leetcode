#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#
# https://leetcode.com/problems/meeting-rooms/description/
#
# algorithms
# Easy (57.71%)
# Total Accepted:    371.9K
# Total Submissions: 644.4K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals where intervals[i] = [starti, endi],
# determine if a person could attend all meetings.
# 
# 
# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: true
# 
# 
# Constraints:
# 
# 
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti < endi <= 10^6
# 
# 
#
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
