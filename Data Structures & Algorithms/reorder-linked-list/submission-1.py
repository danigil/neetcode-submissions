# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> None:
        curr=head
        prev=None
        while curr is not None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        tmp=head
        # count len
        n=0
        while tmp is not None:
            n+=1
            tmp=tmp.next

        mid=n//2
        tmp=head
        for _ in range(mid):
            tmp=tmp.next
        
        head1=head
        head2=tmp
        # if head2:
        #     print(f'h2 {head2.val} -> {head2.next.val if head2.next else ""}')
        head2=self.reverseList(head2)
        # print(f'h1 {head1.val} -> {head1.next.val}')
        # if head2:
        #     print(f'h2 {head2.val} -> {head2.next.val if head2.next else ""}')

        while head1 or head2:
            
            tmp1=head1.next if head1 else None
            tmp2=head2.next if head2 else None

            if head1:
                print(f'head1: {head1.val}')
                head1.next=head2
                head1=tmp1
            
            if head2:
                print(f'head2: {head2.val}')
                head2.next=head1
                head2=tmp2


        