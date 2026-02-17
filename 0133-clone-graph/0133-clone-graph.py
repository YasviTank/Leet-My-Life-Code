"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
## OPTIONAL HERE MEANS THAT THE NODE GIVEN CAN BE None, THAT IS WHAT IS IMPORTED.
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hashmap = {}

        stack = []
        stack.append(node)

        visited = set()
        visited.add(node)

        while stack:
            old_node = stack.pop()
            new_node = Node(val = old_node.val)
            hashmap[old_node] = new_node

            for n in old_node.neighbors:
                if n not in visited:
                    new_node = Node(val = n.val)
                    visited.add(n)
                    stack.append(n)
        
        for old_node, new_node in hashmap.items():
            for n in old_node.neighbors:
                new_n = hashmap[n]
                new_node.neighbors.append(new_n)


        return hashmap[node]

        

        