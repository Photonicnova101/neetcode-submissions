# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        levels = []
        q = deque()
        q.append(root)
        levels.append([root.val])
        i=1
        output = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if (node.left or node.right) and i>=len(levels):
                    levels.append([])
                if node.left:
                    levels[i].append(node.left.val)
                    q.append(node.left)
                if node.right:
                    levels[i].append(node.right.val)
                    q.append(node.right)
            i+=1
        for level in levels:
            output.append(level[-1])
        return output
        


