# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node=head
        if node is None:
            return False
        hashset=set()
        while(node.next is not None):
            if node in hashset:
                return True
            hashset.add(node)
            node=node.next
        return False
        