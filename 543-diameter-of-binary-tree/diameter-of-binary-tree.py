# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #diameter=height_of_left + height_of_right
        res=0
        def height(root):
            nonlocal res
            if not root:
                return 0
            left=height(root.left)
            right=height(root.right)
            res = max(res, left + right)
            return 1+max(left,right)
        height(root)
        print(res)
        return res
        
        