# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS, 
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def funky(node): # return true if NO leafs found
            if node.left:
                node.left = funky(node.left)
            if node.right:
                node.right = funky(node.right)

            if not node.left and not node.right and node.val == target:
                return None
            return node

        return funky(root)

