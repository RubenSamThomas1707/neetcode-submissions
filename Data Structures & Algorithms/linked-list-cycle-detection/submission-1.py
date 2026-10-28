# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Good solutino: But O(N) space
        # visited = set()
        # curr = head

        # while curr:
        #     if curr in visited:
        #         return True
            
        #     visited.add(curr)
        #     curr = curr.next
        
        # return False

        # *************
        # Optimal Solution: O(1) space
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False