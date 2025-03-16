# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        hashmap=defaultdict(list)
        level=0
        queue=collections.deque()
        queue.append([root,level])
        while queue:
            len_queue=len(queue)
            while(len_queue!=0):
                root,level=queue.popleft()
                hashmap[level].append(root.val)
                if root.left: queue.append([root.left,level+1])
                if root.right: queue.append([root.right,level+1])
                len_queue-=1
            level+=1
        res=[]
        for i in range(0,level):
            res.append(hashmap[i][-1])
        return res
        


        