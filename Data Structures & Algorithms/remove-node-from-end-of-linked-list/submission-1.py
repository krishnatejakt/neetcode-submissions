# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        length = 0
        while temp!=None:
            length+=1
            temp = temp.next
        
        index = length - n

        if index == 0:
            return head.next

        prev, curr = None, head

        while index!=0:
            nxt = curr.next
            prev = curr
            curr = nxt
            index-=1

        prev.next = curr.next
        return head


        
        
        
        