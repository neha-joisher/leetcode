# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        hashset=set()
        node=head
        while node!=None:
            if node in hashset:
                return True
            hashset.add(node)
            node=node.next
        return False
        # slow=fast=head
        # while fast  and fast.next:
        #     slow=slow.next
        #     fast=fast.next.next
        #     if slow==fast:
        #         return True
        # return False
        