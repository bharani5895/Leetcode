# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next
      
      
      
      
      
      
      
      
      
      
      
      
        """ if head is not None and node<=0:
            return None

        curr=head
        if curr.next is not None:
            after=curr.next

        while curr.next is not None:
            if curr.x == node:
                curr.next=head

            if curr.next == node:
                curr.next=after.next
                after.next=curr.next
            
            else:
                curr=after

            after=after"""
        