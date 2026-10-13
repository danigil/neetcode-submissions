# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     return self.reverse(head, None)
    # def reverse(self, curr: Optional[ListNode], prev: Optional[ListNode]):
    #     if not curr:
    #         return curr

    #     tmp=curr.next
    #     curr.next=prev
    #     if not tmp:
    #         return curr
    #     return self.reverse(tmp, curr)
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
    def print_ll(self, head: Optional[ListNode]):
        s=""
        curr=head
        while curr.next is not None:
            s+=f'{curr.val} -> '
            curr=curr.next
        s+=f'{curr.val}'
        print(s)

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        rev = self.reverseList(head)
        
        if n==1:
            return self.reverseList(rev.next)
        
        prev=None
        curr=rev
        newhead=rev
        i=2
        while i<n:
            prev=curr
            curr=curr.next
            
            i+=1

        curr.next=curr.next.next
        self.print_ll(curr)

        while curr.next is not None:
            curr=curr.next

        self.print_ll(self.reverseList(curr))
        return self.reverseList(newhead)
        