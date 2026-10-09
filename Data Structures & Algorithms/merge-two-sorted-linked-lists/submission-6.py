# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            if list1 is None:
                return list2
            else:
                return list1
        
        if list1.val <= list2.val:
            head=list1
            rest=self.mergeTwoLists(list1.next,list2)
            head.next=rest
            return head
        else:
            head=list2
            rest=self.mergeTwoLists(list1,list2.next)
            head.next=rest
            return head
        