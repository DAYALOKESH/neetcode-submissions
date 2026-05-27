# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subRoot is empty, it's always a subtree
        if not subRoot:
            return True
        # If root is empty (and subRoot isn't), subRoot can't be a subtree
        if not root:
            return False
        
        # Check if the tree starting at *this* root is the same
        if self.sameTree(root, subRoot):
            return True
            
        # *** THIS IS THE FIX ***
        # If not, check if subRoot is a subtree of root's left OR right child
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # Your sameTree helper function is perfect!
    def sameTree(self, root, subRoot):
        # If both are empty, they are the same
        if not root and not subRoot:
            return True
        
        # If both are non-empty and their values match
        if root and subRoot and root.val == subRoot.val:
            # Check that their left and right subtrees are also the same
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
            
        # If one is empty, or values don't match, they aren't the same
        return False