class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            middle = left + (right - left) // 2

            # print(f"{left = } | {middle = } | {right = }")
            # print(f"{nums[left] = } | {nums[middle] = } | {nums[right] = }")

            if nums[middle] == target:
                return middle
            
            elif nums[middle] < target:
                left = middle + 1
            
            else:
                right = middle - 1

            # print("***********")
        
        # print(f"{left = } | {middle = } | {right = }")
        # print(f"{nums[left] = } | {nums[middle] = } | {nums[right] = }")
        
        return right + 1