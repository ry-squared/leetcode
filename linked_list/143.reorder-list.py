#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (55.00%)
# Total Accepted:    778.3K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3,4]'
#
# You are given the head of a singly linked-list. The list can be represented
# as:
# 
# 
# L0 → L1 → … → Ln - 1 → Ln
# 
# 
# Reorder the list to be on the following form:
# 
# 
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 
# 
# You may not modify the values in the list's nodes. Only nodes themselves may
# be changed.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 1000
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ast import List
class Solution:

    def getListMidpoint(self, head: ListNode) -> ListNode:
        # find the middle of linked list [Problem 876]
        # in 1->2->3->4->5->6 find 4
        slow_head = head
        fast_head = head
        while fast_head and fast_head.next:
            slow_head = slow_head.next
            fast_head = fast_head.next.next 
        return slow_head
    
    def reverseList(self, head: ListNode) -> ListNode:
        # reverse the second part of the list [Problem 206]
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        prev_head = None
        curr_head = head
        while curr_head:
            next_head = curr_head.next

            curr_head.next = prev_head
            prev_head = curr_head
            
            curr_head = next_head

        return prev_head

    def mergeLists(self, head: ListNode, rev_second: ListNode) -> ListNode:
        # merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first = head
        second =  rev_second
        while second.next:

            first_next = first.next # temp var
            first.next = second
            first = first_next # reset with temp var

            second_next = second.next # temp var
            second.next = first
            second = second_next # reset with temp var

    def reorderList(self, head: ListNode) -> None:

        second=self.getListMidpoint(head=head)
        second_rev=self.reverseList(head=second)
        self.mergeLists(head=head,rev_second=second_rev)
