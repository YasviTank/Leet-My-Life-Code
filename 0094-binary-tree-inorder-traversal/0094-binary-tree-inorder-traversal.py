# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        result = []
        current = root
        
        while current or stack:
            # go left as far as possible
            while current:
                stack.append(current)
                current = current.left
            
            # visit node
            current = stack.pop()
            result.append(current.val)
            
            # go right
            current = current.right
        
        return result
