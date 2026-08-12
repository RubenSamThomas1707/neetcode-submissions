# class MyHashSet:

#     def __init__(self):
#         self.hset = {}

#     def add(self, key: int) -> None:
#         self.hset[key] = 1

#     def remove(self, key: int) -> None:
#         self.hset[key] = 0

#     def contains(self, key: int) -> bool:
#         return self.hset.get(key, 0) != 0


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# Array Approach
class MyHashSet:

    def __init__(self):
        self.hset=[]

    def add(self, key: int) -> None:
        if key not in self.hset:
            self.hset.append(key)

    def remove(self, key: int) -> None:
        if key in self.hset:
            self.hset.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hset