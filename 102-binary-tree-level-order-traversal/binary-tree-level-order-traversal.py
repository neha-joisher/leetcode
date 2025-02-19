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
        while(queue):
            len_level=len(queue)
            res.append([])
            for i in range(len_level):
                current=queue.popleft()
                print(current.val)
                res[level].append(current.val)
                print(res)
                # print(queue)
                if current.left:queue.append(current.left)
                if current.right:queue.append(current.right)
            level+=1
        print(res)
        return res
        