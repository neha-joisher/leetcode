# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val>q.val:
            temp=q
            q=p
            p=temp
        print(root.val,p.val,q.val)
        if root.val>=p.val and root.val<=q.val:
            print("First if")
            return root
        elif root.val>=p.val and root.val>q.val:
            print("second if")
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            print("else")
            return self.lowestCommonAncestor(root.right,p,q)
