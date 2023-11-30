#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (75.08%)
# Total Accepted:    3.6M
# Total Submissions: 4.7M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, reverse the list, and return the
# reversed list.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
#
# Example 2:
#
#
# Input: head = [1,2]
# Output: [2,1]
#
#
# Example 3:
#
#
# Input: head = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
#
#
#
# Follow up: A linked list can be reversed either iteratively or recursively.
# Could you implement both?
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ll = None
        ll_prev = None
        head_current = head

        # doesn't work; this updates head_current too
        # ll = head_current
        # ll.next = None

        while head_current != None:
            head_next = head_current.next
            # ll = ListNode(val=head_current.val, next=ll)
            ll = head_current
            ll.next = ll_prev
            ll_prev = ll
            head_current = head_next #reassigns head_current w/o changing ll
        return ll

# Example ListNode
#
# class ListNode:
#      def __init__(self, val=0, next=None):
#          self.val = val
#          self.next = next
# ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None)))))