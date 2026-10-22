class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Simple O(n) solution
        # Loop through the elements in teh array
        # Check if current element is less that the current min
        # Yes then update min
        # Otherwise continue
        # Finally return min

        minNum = nums[0]
        for idx in range(1, len(nums)):
            minNum = min(minNum, nums[idx])
        
        return minNum

        # ******************
        left, right = 0, len(nums) - 1
        minVal = float('inf')

        while left <= right:
            middle = left + (right - left) // 2
            print(f"{middle = } | {nums[middle] = }")
            print(f"{nums[left] = } | {nums[right] = }")

            minVal = min(minVal, nums[middle])

            if nums[left] <= nums[middle] <= nums[right]:
                right = middle - 1
            else:
                left = middle + 1

            print("*********")

        return minVal
            


