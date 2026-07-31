# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummyeven=head.next
        
        odd=head
        even=head.next

        while even != None and even.next != None:
            odd.next=odd.next.next
            odd=odd.next


            even.next=even.next.next
            even=even.next

        odd.next=dummyeven
        return head