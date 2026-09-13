# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowPointer = head
        fastPointer = head

        while head:
            slowPointer = slowPointer.next
            if fastPointer.next and fastPointer.next.next:
                fastPointer = fastPointer.next.next
            else: return False

            if slowPointer == fastPointer:
                return True
            head = head.next
        return False
            