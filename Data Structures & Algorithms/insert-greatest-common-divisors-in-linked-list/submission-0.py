# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        dummy2 = head
        toinsert = []
        stack = []
        while head:
            stack.append(head.val)
            if len(stack)==2:
                toinsert.append(math.gcd(stack[0],stack[1]))
                stack.pop(0)
            head = head.next
        counter = 0
        while dummy and toinsert:
            if counter==0:
                temp = dummy.next
                dummy.next = ListNode(toinsert.pop(0),temp)
                dummy.next.next = temp
                counter=1
                dummy = dummy.next
            else:
                counter-=1
                dummy = dummy.next
        return dummy2

        
            