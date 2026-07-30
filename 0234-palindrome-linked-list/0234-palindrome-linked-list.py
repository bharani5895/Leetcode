# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Helper function to reverse the list starting from a given node
        def reverselist(left: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            curr = left
            while curr is not None:
                after = curr.next  # Save next node before changing link
                curr.next = prev   # Reverse pointer
                prev = curr        # Advance prev
                curr = after       # Advance curr
            return prev

        # 1. Find the middle of the linked list
        fast = head
        slow = head
        prev = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # 2. Reverse the second half (starting from slow)
        second_half = reverselist(slow)

        # 3. Compare the first half and reversed second half
        p1 = head
        p2 = second_half
        while p2 is not None:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True