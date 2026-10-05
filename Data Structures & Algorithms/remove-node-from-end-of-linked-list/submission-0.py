# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        cur = head
        nodes = []
        while cur:
            nodes.append(cur)
            cur = cur.next
        if len(nodes)==1:
            return
        if n==1:
            nodes[-2].next = None
            return nodes[0]
        if n==len(nodes):
            return nodes[1]
        nodes[-n-1].next = nodes[-n+1]
        return nodes[0]

        
        