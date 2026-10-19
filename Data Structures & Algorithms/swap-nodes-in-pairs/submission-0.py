# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode(0,head)
        
        while True:
            if not head.next:
                break
            if not head.next.next:
                break

            prev = head
            n1 = head.next
            n2 = head.next.next
            
            prev.next = n2
            n1.next = n2.next
            n2.next=n1

            head = head.next.next
        
        return dummy.next