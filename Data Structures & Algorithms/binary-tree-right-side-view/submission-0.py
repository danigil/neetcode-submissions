# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ret=[]
        # q=deque([root])
        # nextq=deque([])
        q=[root]
        while q:
            nextq=[]
            for i,curr in enumerate(q):
                if not curr:
                    continue
                if i==0:
                    ret.append(curr.val)
                # nextq += [curr.right, curr.left]
                if curr.right:
                    nextq.append(curr.right)
                if curr.left:
                    nextq.append(curr.left)
            q=nextq
            # curr=q.popleft()
            # if curr:
            #     q.extendright([curr.right, curr.left])
            
            # ret.append(curr.val)

            # if curr.right:
            #     q.append(curr.right)
            # elif curr.left:
            #     q.append(curr.left)
        return ret
            # q.append(curr.right)

        