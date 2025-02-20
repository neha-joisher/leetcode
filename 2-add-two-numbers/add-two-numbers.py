# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        node=dummy
        carry_forward=0
        while l1 != None or l2 != None or carry_forward != 0:
            new_node=ListNode()
            l1Val= l1.val if l1 else 0
            l2Val= l2.val if l2 else 0
            sum=l1Val + l2Val+carry_forward
            if sum>9:
                new_node.val=sum%10
                carry_forward=(sum//10)%10
                print(carry_forward)
            else:
                carry_forward=0
                new_node.val=sum
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            node.next=new_node
            node=node.next
        print(dummy.next)
        return dummy.next
        