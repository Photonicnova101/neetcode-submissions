# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        strin = ""
        while head:
            strin+=""+str(head.val)
            head =head.next
        return strin[::-1]==strin