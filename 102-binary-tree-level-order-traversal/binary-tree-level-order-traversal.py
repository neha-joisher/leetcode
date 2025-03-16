# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        queue=deque()
        queue.append(root)
        level=0
        while queue:
            len_queue=len(queue)
            res.append([])
            while (len_queue!=0):
                curr=queue.popleft()
                res[level].append(curr.val)
                if curr.left:queue.append(curr.left)
                if curr.right:queue.append(curr.right)
                len_queue-=1
            level+=1
        return res
        