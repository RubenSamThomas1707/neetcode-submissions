"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummyNew = Node(0)
        currNode = dummyNew
        currOld = head
        old_to_new = {}

        while currOld:
            newNode = Node(currOld.val)
            currNode.next = newNode
            old_to_new[currOld] = newNode
            
            currNode = currNode.next
            currOld = currOld.next

        currOld = head
        currNode = dummyNew.next
        while currOld:
            if currOld.random is not None:
                currNode.random = old_to_new[currOld.random]
            else:
                currNode.random = None            

            currOld = currOld.next
            currNode = currNode.next

        return dummyNew.next

