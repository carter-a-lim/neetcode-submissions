# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseListHelper(node, rest) -> Optinal[ListNode]:
            if not rest:
                return node
            
            node = ListNode(rest.val, node)
            return reverseListHelper(node, rest.next)
            
        return reverseListHelper(None, head)


        """ ITERATIVE SOLUTION
        output = None

        if head==None:
            return head

        while head.next:
            output = ListNode(head.val, output)
            head = head.next
        output = output = ListNode(head.val, output)

        return output
        """