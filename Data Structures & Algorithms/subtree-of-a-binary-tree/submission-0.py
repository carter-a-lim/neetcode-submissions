# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # handle edge cases
        if not subRoot:
            return True
        if not root:
            return False
        
        # subfunction to find out if given nodes are same tree
        def treeCheck(root, subtree):
            if root is None and subtree is None:
                return True

            if root and subtree and root.val == subtree.val:
                return treeCheck(root.left, subtree.left) and treeCheck(root.right, subtree.right)
            return False

        # check every node for if its subtree
        if treeCheck(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
 
        