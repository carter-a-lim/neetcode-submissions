# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = [] # seen values
        # if node.val in seen: return true
        pointer = head

        if head == None:
            return False

        while pointer.next != None:
            if pointer.val in seen:
                return True
            else:
                seen.append(pointer.val)
                pointer = pointer.next
        return False