class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Approach 1: O(N) time - O(N) space
        # seen = set()

        # for num in nums:
        #     if num in seen:
        #         return num
            
        #     seen.add(num)
        
        # return -1

        # *****************
        # Approach 2: Treating array as linked list and slow and fast pointers
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
                
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow