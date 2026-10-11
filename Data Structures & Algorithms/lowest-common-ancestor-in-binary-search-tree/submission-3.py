# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def canReach(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if root is None or p is None:
            return False
        
        if root.val==p.val:
            return True
        
        if root.val<p.val:
            return self.canReach(root.right, p)
        else:
            return self.canReach(root.left,p)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return root

        if p.val > q.val:
            tmp=p
            p=q
            q=tmp
        
        if p.val <= root.val <= q.val:
            return root
        elif p.val <= root.val and q.val <= root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        
        



        
        