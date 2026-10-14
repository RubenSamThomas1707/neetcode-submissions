class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Reverse entire array
        # Reverse first 0 - k elements
        # Then reverse k+1 to len(nums) elements

        # Reverse entire array
        l, r = 0, len(nums) - 1
        k %= len(nums)

        # print(f"Original array: {nums = }")
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # print(f"Reversed array: {nums = }")

        # Reverse first k elements
        l, r = 0, k-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        # print(f"Reversed first k elements: {nums = }")

        # Reverse k+1 to len(n) elements
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        # print(f"Final array: {nums = }")
