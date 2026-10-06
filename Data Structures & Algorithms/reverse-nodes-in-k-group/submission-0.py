# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        # reverse each full group of k in the array
        for start in range(0, len(nodes) - k + 1, k):
            nodes[start:start + k] = nodes[start:start + k][::-1]

        # relink everything in the new order
        for a, b in zip(nodes, nodes[1:]):
            a.next = b
        nodes[-1].next = None

        return nodes[0]
        
