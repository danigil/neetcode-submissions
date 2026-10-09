# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ret=None
        curr1=list1
        curr2=list2
        flag=True

        while curr1 is not None or curr2 is not None:
            if curr1 is not None and curr2 is not None:
                if curr1.val <= curr2.val:
                    winner=curr1
                    curr1=curr1.next
                else:
                    winner=curr2
                    curr2=curr2.next
            elif curr1 is not None:
                winner=curr1
                curr1=curr1.next
            else:
                winner=curr2
                curr2=curr2.next

            if flag:
                # ret.val=winner.val
                ret=winner
                flag=False
                prev=ret
            else:
                prev.next=winner
                prev=winner
            

            
            
        return ret
            

        