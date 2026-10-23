# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # traverse, get length
        # traverse again, remove
        length = 1
        lengther = pointer = head
        while lengther.next:
            lengther = lengther.next
            length += 1

        if length == 1:
            return None
        if length == n:
            return head.next

        for _ in range(length-n-1):
            pointer = pointer.next

        pointer.next = pointer.next.next
        return head

        

