# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # for each node, if lt or gt both nums, root node must be other, 
        # go till find node where one is gt one is lt
        if min(p.val,q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if max(p.val,q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
        
        # root.val must be within [p,q]:
