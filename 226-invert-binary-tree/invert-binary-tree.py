# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue=deque()
        queue.append(root)
        while queue:
            current=queue.popleft()
            print(current.val)
            current.left, current.right = current.right, current.left
            if current.right:queue.append(current.right)
            if current.left:queue.append(current.left)
        return root
        