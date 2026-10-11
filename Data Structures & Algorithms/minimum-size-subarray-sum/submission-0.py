class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        currSum = 0
        minSize = float('inf')
        
        for right in range(len(nums)):
            currSum += nums[right]
            while currSum >= target:
                minSize = min(minSize, right - left + 1)
                currSum -= nums[left]
                left += 1

        return minSize if minSize != float('inf') else 0