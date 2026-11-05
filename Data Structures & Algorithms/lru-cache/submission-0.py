class LRUCache:

    class Node:
        def __init__(self, key=0, val=0, left=None, right=None):
            self.key = key
            self.val = val
            self.left = left
            self.right = right

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}
        
        # Create dummy head and tail
        self.head = self.Node()
        self.tail = self.Node()
        self.head.right = self.tail
        self.tail.left = self.head

    def _remove(self, node):
        # Helper to cut node out of the list
        prevNode = node.left
        nextNode = node.right
        prevNode.right = nextNode
        nextNode.left = prevNode

    def _add_to_front(self, node):
        # Helper to insert node right after dummy head (Most Recent)
        nextNode = self.head.right
        self.head.right = node
        node.left = self.head
        node.right = nextNode
        nextNode.left = node

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        
        node = self.mapping[key]
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            # Update existing node and move to front
            node = self.mapping[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.mapping) >= self.capacity:
                # Evict LRU node (the one right before dummy tail)
                lru = self.tail.left
                self._remove(lru)
                del self.mapping[lru.key]
            
            # Create new node and add to front and mapping
            newNode = self.Node(key, value)
            self._add_to_front(newNode)
            self.mapping[key] = newNode
        
