# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head, None)
    def reverse(self, curr: Optional[ListNode], prev: Optional[ListNode]):
        if not curr:
            return curr
        
        # head.next=reverse(head.next)
        # tmp=head.next.next
        # head.next.next=head
        # return head
        tmp=curr.next
        curr.next=prev
        if not tmp:
            return curr


        

        return self.reverse(tmp, curr)
        