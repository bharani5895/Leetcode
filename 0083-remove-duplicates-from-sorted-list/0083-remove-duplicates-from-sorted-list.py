# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        curr=head
        if curr.next is not None:
            after=curr.next
        
        while curr.next is not None:
            if curr.val==after.val:
                curr.next=after.next
                after.next=curr.next
            
            else:
                curr=after
        
            after=after.next
        
        return head