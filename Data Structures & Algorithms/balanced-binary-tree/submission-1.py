# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1+max(self.height(root.left), self.height(root.right))
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        hl = self.height(root.left)
        hr = self.height(root.right)
        h = 1 + max(hl,hr)

        return (abs(hl-hr) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)
        