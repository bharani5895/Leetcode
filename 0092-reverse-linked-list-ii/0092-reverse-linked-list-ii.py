# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverselist(leftnode: Optional[ListNode],rightnext: int) -> Optional[ListNode]:
            prev=rightnext
            curr=leftnode
            after=leftnode.next

            while( curr != rightnext):
                curr.next=prev
                prev=curr
                curr=after
                if after!=rightnext:
                    after=after.next

            return prev

        if(head.next == None):
            return head
        dummynode=ListNode(0)
        dummynode.next=head
        leftprt=head
        rightprt=head
        prevleft=head
        if left ==1:
            prevleft=dummynode

        while(leftprt != None and left != 1):
            prevleft=leftprt
            left-=1
            leftprt=leftprt.next

        while rightprt !=None and right!=1:
            right-=1
            rightprt=rightprt.next
        if leftprt == None or rightprt ==None:
            return head
        prevleft.next=reverselist(leftprt,rightprt.next)
        return dummynode.next 
