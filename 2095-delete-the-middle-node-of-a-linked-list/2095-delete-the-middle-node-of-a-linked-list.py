# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            head=head.next
            return head
             
        fast = head
        slow = head
        prev=None
        while(fast != None and fast.next !=None):
            fast=fast.next.next
            prev=slow
            slow=slow.next

        prev.next=prev.next.next
        return head