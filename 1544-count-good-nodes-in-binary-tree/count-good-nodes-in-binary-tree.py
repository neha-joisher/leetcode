# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def dfs(root,max_Value):
            nonlocal count
            if not root:
                return 
            if root.val>=max_Value:
                count+=1
                max_Value=root.val
            dfs(root.left,max_Value)
            dfs(root.right,max_Value)
        dfs(root,root.val)
        return count
        