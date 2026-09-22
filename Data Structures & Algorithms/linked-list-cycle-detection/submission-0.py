# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = {}

        while head!=None:
            if head not in d:
                d[head] = 1
            else:
                return True
            head = head.next
        return False
        