# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        prev=None
        curr=head
        after=head.next

        while curr!=None:
            curr.next=prev
            prev=curr
            curr=after
            if after!=None:
                after=after.next

        return prev