# 3/19/2024
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):

        pointer = list1
        for x in range (a - 1):
            pointer = pointer.next

        bpointer = pointer.next
        for x in range (b - a + 1):
            bpointer = bpointer.next
        
        pointer.next = list2
        while pointer.next != None:
            pointer = pointer.next

        pointer.next = bpointer

        return list1 


        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """