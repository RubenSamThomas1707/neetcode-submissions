class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Not Optimal. Starting solution: O(N) Time and Space complexity
        # n = len(nums)
        # exists = [False] * n

        # for num in nums:
        #     if num > 0 and num <= n:
        #         exists[num - 1] = True

        # for i in range(n):
        #     if not exists[i]:
        #         return i + 1
        
        # return (n + 1)

        # ***********
        
        # Set negative values to 0
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        # Loop through nums list and mark indexes to be negative if they are within 1 to len(n) limit
        for num in nums:
            if num == 0:
                continue
            val = abs(num)
            # Only accounting for values between the 1 to len(nums) range
            if val > 0 and val <= n:
                # If value is 0, then it was previously negative, so replacing it with -1 * val
                if nums[val - 1] == 0:
                    nums[val - 1] = -1 * val
                # If value is positive, then marking it as negative to indicate value is present
                elif nums[val - 1] > 0:
                    nums[val - 1] *= -1
                # If value is already negative, then that value already exists and is visited, so keeping it unchanged
                else:
                    continue

        # Looping through list to find first non-negative value
        for i, v in enumerate(nums):
            if v >= 0:
                return i + 1

        # If all values are negative in nums, then we have all values from 1 to len(nums) exist, so next smallest is (n + 1)
        return (n + 1)






