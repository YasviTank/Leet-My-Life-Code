# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
         # base case: 0 or 1 node left → no swap
        if not head or not head.next:
            return head
        
        first = head
        second = head.next
        
        # recursively swap remaining list
        first.next = self.swapPairs(second.next)
        
        # swap current pair
        second.next = first
        
        return second
