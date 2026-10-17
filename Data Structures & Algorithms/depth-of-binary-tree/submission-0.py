# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root, curr):
            if root is None:
                return curr

            if root.left is None:
                return depth(root.right, curr+1)
            
            if root.right is None:
                return depth(root.left, curr+1)

            return max(depth(root.left, curr+1), depth(root.right, curr+1))
        
        return depth(root, 0)