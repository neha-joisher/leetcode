# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]

        def InOrder(root):
            if not root:
                return  
            InOrder(root.left)
            res.append(root.val)
            InOrder(root.right)
        InOrder(root)
        print(res)
        return res[k-1]
        