# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        ################### to find the middle
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        ################### to reverse the links
        start=slow.next
        prev=None
        #to end the first list
        slow.next=None 

        while(start is not None):
            temp=start.next
            start.next=prev
            prev=start
            start=temp
        #prev is head

        ################### merging both the lists
        n1=head
        n2=prev
        while n2:
            t1=n1.next
            t2=n2.next
            n1.next=n2
            n2.next=t1
            n1=t1
            n2=t2
        