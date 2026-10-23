class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute force: O(N)
        # for i, v in enumerate(nums):
        #     if v == target:
        #         return i
            
        # return -1

        # *****************
        # Approach 2: Binary Search
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return middle
            
            # Check if the left half is sorted
            if nums[left] <= nums[middle]:
                # Check if target lies within the sorted left half
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            # Otherwise, the right half must be sorted
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        
        return -1