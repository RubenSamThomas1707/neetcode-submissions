# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head

        while curr is not None:
            next = curr.next

            dummyNext = dummy.next
            dummy.next = curr
            curr.next = dummyNext
            curr = next
        
        return dummy.next