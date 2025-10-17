"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # None : None is for the edge case when the random pointer points to Null
        copymap = {None : None}

        curr = head
        while curr:
            copy = Node(curr.val)
            copymap[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = copymap[curr]
            copy.next = copymap[curr.next]
            copy.random = copymap[curr.random]
            curr = curr.next

        return copymap[head]
        