# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        occur = set()
        p = head

        while p:
            if p in occur:
                return True
            occur.add(p)
            p = p.next
        return False