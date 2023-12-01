#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (63.42%)
# Total Accepted:    3.7M
# Total Submissions: 5.8M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# You are given the heads of two sorted linked lists list1 and list2.
# 
# Merge the two lists into one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
# 
# Return the head of the merged linked list.
# 
# 
# Example 1:
# 
# 
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# 
# 
# Example 2:
# 
# 
# Input: list1 = [], list2 = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: list1 = [], list2 = [0]
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1,list2):

        llm = ListNode()
        curr_llm = llm # curr_llm is pointer to llm
        while list1!=None and list2!=None:

            if list1.val < list2.val:
                curr_llm.next = list1 # assign next link in curr_llm to list1, also upates llm.next
                list1 = list1.next  # assign next link in list1 to list 1, basically popping the head off
            else:
                curr_llm.next = list2 # similar to above
                list2 = list2.next

            # re-assign next curr_llm to next link in curr_llm, i.e. a new memory address
            # next time we modify curr_llm the next link in llm is modified
            curr_llm = curr_llm.next

        # add leftover list
        if list1==None:
            curr_llm.next = list2
        else:
            curr_llm.next = list1

        return(llm.next)