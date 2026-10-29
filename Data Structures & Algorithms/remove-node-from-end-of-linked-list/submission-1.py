# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 2 * O(N) approach - Not optimal
        # length = 0
        # curr = head

        # while curr:
        #     length += 1
        #     curr = curr.next
        
        # dummy = ListNode(next = head)
        # curr = dummy
        # for i in range(length - n):
        #     print(i)
        #     curr = curr.next
        
        # curr.next = curr.next.next
        
        # return dummy.next

        # ***************
        # Approach 2: O(N) - One pass
        dummy = ListNode(next = head)
        left, right = dummy, dummy

        for i in range(n):
            right = right.next
        
        while right.next:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next
