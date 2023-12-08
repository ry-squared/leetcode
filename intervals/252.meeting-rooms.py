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
        
        min_end = 99999
        max_end = 0
        min_start = 99999
        max_start = 0
        for i in range(len(intervals)-1):

            a = intervals[i][0]
            b = intervals[i][1]

            if a < min_start:
                min_start = a
            if b > max_end:
                max_end = b

            if a > max_start:
                max_start = a
            if b < min_end:
                min_end = b
            
            a_next = intervals[i+1][0]
            b_next = intervals[i+1][1]

            # check if new interval is before first meeting OR 
            # after last meeting OR between meetings
            if (a_next >= max_end) or \
                (b_next <= min_start) or \
                  (a_next >= min_end and b_next <= max_start):
                continue

            return False

                    
        return(True)