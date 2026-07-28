# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None and n==1:
            return None

        i=head
        j=head
        prev=head
        l=1

        while(l<n):
            j=j.next
            if j ==None :
                return head
            l+=1

        if j.next == None:
            return head.next

        while(j.next != None):
            prev=i
            i=i.next
            j=j.next

        
        prev.next=i.next

        return head