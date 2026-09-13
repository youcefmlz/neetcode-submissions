# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous , current = None , head
        t=None
        while(current):
            t = current.next
            current.next = previous
            previous = current
            current = t

        return previous 

    