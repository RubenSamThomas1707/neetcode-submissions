class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Pseudocode
        # Sort the array
        # Create a for (index = i) loop from 0, to len(nums) - 3
            # Create a second (index = j) for loop from (i + 1) to len(nums) - 2
                # Initialize left (j + 1) and right (len(nums) - 1) pointers
                # Loop while left < right:
                    # If nums[i] + nums[j] + nums[left] + nums[right] == target
                        # Add them to the list
                        # While left pointer elements are equal, keep moving left
                        # While right pointers are equal, keep moving right inwards
                        # Increment and decrement pointers as needed
                    # If currSum < target, move left pointer to the right
                    # If currSum > target, move right pointer to the left    
        # Return final list with the results

        # -----------

        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return res