# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        k = k%length
        if k == 0:
            return head

        diff = length - k
        curr = head
        for i in range(length - k - 1):
            curr = curr.next
        newhead = curr.next
        curr.next = None

        tail.next = head
        head = newhead

        return head



