"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        
        curr = head
        while curr is not None:
            # if the current node has a child then flatten the child first
            if curr.child is not None:
                next_node = curr.next
                
                child_tail = curr.child
                while child_tail.next is not None:
                    child_tail = child_tail.next
                
                if next_node is not None:
                    child_tail.next = next_node
                    next_node.prev = child_tail
                
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            
            # move forward if the curr node has no child
            curr = curr.next
        
        return head
        