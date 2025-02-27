"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        if head == None:
            return None

        stack = []
        curr = head

        while curr:
            if curr.child:
                # If there's a next node, push it to the stack to process later
                if curr.next:
                    stack.append(curr.next)
                    curr.next.prev = None  # Detach prev pointer to avoid cycles

                # Connect child as the next node
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None  # Set child to None

            if not curr.next and stack:
                # If we've reached the end of a level, pop the next node from the stack
                curr.next = stack.pop()
                curr.next.prev = curr

            curr = curr.next

        return head