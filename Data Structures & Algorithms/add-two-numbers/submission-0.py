# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # O(N) or O(M) - whichevers longer
        # O(N) or O(M) whichever is longer
        # num1, num2 = 0, 0
        
        # currHead = l1
        # currMultiplier = 1

        # while currHead:
        #     num1 += (currMultiplier * currHead.val)
        #     currMultiplier *= 10
        #     currHead = currHead.next
        
        # currHead = l2
        # currMultiplier = 1

        # while currHead:
        #     num2 += (currMultiplier * currHead.val)
        #     currMultiplier *= 10
        #     currHead = currHead.next
        
        # total = num1 + num2

        # if total == 0:
        #     return ListNode(0)

        # dummyNode = ListNode()
        # currHead = dummyNode
        
        # while total > 0:
        #     newNode = ListNode(total % 10)
        #     currHead.next = newNode
        #     currHead = currHead.next
        #     total //= 10

        # return dummyNode.next

        # **************

        # Approach 2:
        dummyNode, carryOver = ListNode(), 0
        currHead = dummyNode

        while l1 and l2:
            totalSum = l1.val + l2.val + carryOver
            print(f"{totalSum = }")

            currHead.next = ListNode(totalSum % 10)
            carryOver = totalSum // 10

            currHead = currHead.next
            l1, l2 = l1.next, l2.next

        while l1:
            totalSum = l1.val + carryOver
            currHead.next = ListNode(totalSum % 10)
            carryOver = totalSum // 10
            currHead = currHead.next
            l1 = l1.next
        while l2:
            totalSum = l2.val + carryOver
            currHead.next = ListNode(totalSum % 10)
            carryOver = totalSum // 10
            currHead = currHead.next
            l2 = l2.next

        if carryOver > 0:
            currHead.next = ListNode(carryOver)
            
        return dummyNode.next