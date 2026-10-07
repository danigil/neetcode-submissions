# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# import heapq

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        pq = []
        if root:
            pq.append(root)

        while pq:
            curr_l = []
            next_batch = []
            
            for curr in pq:
                if curr:
                    curr_l.append(curr.val)

                    if curr.left:
                        next_batch.append(curr.left)

                    if curr.right:
                        next_batch.append(curr.right)
            
            ret.append(curr_l)
            pq = next_batch
        return ret
        