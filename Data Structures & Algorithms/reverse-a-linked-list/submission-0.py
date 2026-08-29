# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = None
        pointer2 = head

        while pointer2:
            pointer2next = pointer2.next
            pointer2.next = pointer1
            pointer1=pointer2
            pointer2=pointer2next
        return pointer1