"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        curr,nextCurr=root, root.left if Node else None

        while curr and nextCurr:
            curr.left.next=curr.right
            if curr.next:
                curr.right.next=curr.next.left
            curr=curr.next
            if not curr:
                curr=nextCurr
                nextCurr=curr.left
        return root


        # if not root:
        #     return None
        # queue=collections.deque()
        # queue.append(root)

        # while queue:
        #     len_queue=len(queue)

        #     for i in range(len_queue):
        #         current=queue.popleft()
        #         if i<len_queue-1:
        #             current.next=queue[0]
        #         if current.left: queue.append(current.left)
        #         if current.right: queue.append(current.right)
        
        # return root
        