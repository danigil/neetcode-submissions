# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        # ret=ListNode(val=0, next=None)
        # curr=ret
        prev=None
        ret=None
        
        while l1 is not None or l2 is not None or carry>0:
            val1=val2=0
            if l1:
                val1=l1.val
                l1=l1.next
            
            if l2:
                val2=l2.val
                l2=l2.next

            val = val1+val2+carry
            excess = val%10
            carry=val//10

            curr=ListNode(val=excess, next=None)
            if not ret:
                ret=curr
            if prev:
                prev.next=curr
            prev=curr
            # curr.val=excess
            # if excess > 0 or carry > 0:
            #     curr.next=ListNode(val=0, next=None)
            # else:
            #     curr.next=None
            # curr=curr.next



        return ret


                