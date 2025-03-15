# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        carry=0
        while l1 or l2 or carry !=0:
            node1=l1.val if l1 else 0
            node2=l2.val if l2 else 0
            add=node1+node2+carry
            last_digit=add%10
            carry=add//10
            node=ListNode(last_digit)
            curr.next=node
            curr=curr.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next

            


        