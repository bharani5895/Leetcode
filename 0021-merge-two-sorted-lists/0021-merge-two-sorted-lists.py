# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=list1
        temp2=list2
        dummynode=ListNode(-1)
        res=dummynode
        while(temp1 !=None and temp2 != None):
            if temp1.val < temp2.val:
                res.next=temp1
                res=res.next
                temp1=temp1.next
            else:
                res.next=temp2
                res=res.next
                temp2=temp2.next
        
        if temp1 != None:
            res.next=temp1
        
        if temp2 != None:
            res.next=temp2
        
        return dummynode.next