# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(l1: Optional[ListNode], l2: Optional[ListNode], carry: int=0) -> Optional[ListNode]:
            if not l1 and not l2 and carry==0:
                return None

            val1=val2=0
            next1=next2=None
            if l1:
                val1=l1.val
                next1=l1.next
            if l2:
                val2=l2.val
                next2=l2.next
            
            val=val1+val2+carry
            excess=val%10
            nextcarry=val//10

            ret=ListNode(val=excess, next=add(next1,next2,nextcarry))
            return ret

        return add(l1,l2)
        
        