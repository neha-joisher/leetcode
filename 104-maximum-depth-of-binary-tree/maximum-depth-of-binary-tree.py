# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

        # if root is None:
        #     return 0
        # count=0
        # queue=deque()
        # queue.append(root)
        # while(queue):
        #     length=len(queue)
        #     for i in range(length):
        #         current=queue.popleft()
        #         if current.left:queue.append(current.left)
        #         if current.right:queue.append(current.right)
        #     count+=1
        # print(count)
        # return count
        