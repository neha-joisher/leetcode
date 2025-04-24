# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists)==0:
            return None

        while len(lists) > 1:
            mergedList=[]

            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if (i+1)<len(lists) else None
                mergedList.append(self.mergedLists(l1,l2))
            lists = mergedList
        return lists[0]


    def mergedLists(self,l1,l2):
        dummy=node=ListNode()

        while (l1 and l2):
            l1Val=l1.val if l1 else 0
            l2Val=l2.val if l2 else 0

            if l1Val<=l2Val:
                node.next=l1
                l1=l1.next
            else:
                node.next=l2
                l2=l2.next
            node=node.next
        node.next=l1 or l2
        return dummy.next