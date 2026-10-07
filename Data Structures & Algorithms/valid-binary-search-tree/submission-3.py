# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def is_valid(self, )
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, left_lim, right_lim):
                if not node:
                    return True
                
                if not (left_lim < node.val < right_lim):
                    return False

                return check(node.left, left_lim, node.val) and check(node.right, node.val, right_lim)

        return check(root,float("-inf"), float("inf"))




            # if not node:
            #     return True
            # else:
            #     if node.left and node.left.val >= node.val:
            #         return False

            #     if node.right and node.right.val <= node.val:
            #         return False

            #     return (root.left is None or self.isValidBST(root.left)) and (root.right is None or self.isValidBST(root.right))
        