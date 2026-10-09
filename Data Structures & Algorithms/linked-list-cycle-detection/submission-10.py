# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i1, i2 = head, head

        while i2 and i2.next:
            i1=i1.next
            i2=i2.next.next

            if i1 is i2:
                return True
        return False


        