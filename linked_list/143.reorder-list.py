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
    # Q: are 2 node objects that are the same but have diff children equal?

    #alternate nodes from head node forward and last node working backwords until reaching midpoint

    def getMidPoint(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next: # fast.next.next would prematurely terminate on None, whereas we want the last real node
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            
            nxt = cur.next # tmp var
            cur.next = prev
            prev = cur
            cur = nxt

        return prev


    def mergeList(self, head: ListNode, reversedSecondList: ListNode) -> None:

        firstListCur = head
        secondListCur = reversedSecondList

        while secondListCur.next:
            
            # add second list head to first list
            firstListNext = firstListCur.next # tmp var
            firstListCur.next = secondListCur

            # add next node in first list after attached node in second list
            secondListNext = secondListCur.next
            secondListCur.next = firstListNext

            # reset lists to next nodes
            firstListCur = firstListNext
            secondListCur = secondListNext

    def reorderList(self, head: ListNode) -> None:

        midNode = self.getMidPoint(head=head)
        reversedSecondList = self.reverseList(head=midNode)
        self.mergeList(head=head,reversedSecondList=reversedSecondList)