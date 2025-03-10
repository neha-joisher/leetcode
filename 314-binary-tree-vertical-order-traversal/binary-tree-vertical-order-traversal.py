# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=collections.deque()
        queue.append([0,root])
        hashmap_level=defaultdict(list)
        min_col=float("inf")
        max_col=float("-inf")
        res=[]
        while queue:
            level,root=queue.popleft()
            hashmap_level[level].append(root.val)
            min_col = min(min_col, level)
            max_col = max(max_col, level)
            if root.left: queue.append([level-1,root.left])
            if root.right: queue.append([level+1,root.right])

        for i in range(min_col,max_col+1):
            res.append(hashmap_level[i])
        return res

