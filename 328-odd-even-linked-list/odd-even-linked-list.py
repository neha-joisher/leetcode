# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # Nothing to rearrange

        odd = head               # Odd starts at position 1
        even = head.next         # Even starts at position 2
        even_head = even         # Save even head to attach later

        while even and even.next:
            odd.next = even.next  # Link odd to next odd
            odd = odd.next        # Move odd pointer

            even.next = odd.next  # Link even to next even
            even = even.next      # Move even pointer

        odd.next = even_head      # Append even list after odd list
        return head
        