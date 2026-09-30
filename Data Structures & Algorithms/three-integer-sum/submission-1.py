class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute force: O(N^3)
            # Initialize final return list
            # Iterate through the nums list for range in len(nums) - 3
                # Iterate through nums list again for range (i+1) and len(nums) - 2
                    # Iterate through nums list again for range (j+1) and len(nums) - 1
                        # if nums[i] + nums[j] + nums[k] == 0
                            # finalList.append([nums[i] + nums[j] + nums[k]])
            # Return finalList
        
        # Solution:
        # finalList = set()

        # for i in range(len(nums) - 2):
        #     for j in range(i+1, len(nums) - 1):
        #         for k in range(j+1, len(nums)):
        #             if (nums[i] + nums[j] + nums[k]) == 0:
        #                 pairs = tuple(sorted([nums[i],nums[j],nums[k]]))
        #                 finalList.add(pairs)
        
        # return [list(pair) for pair in finalList]

        # -----------------------------------
        # Efficient Solution": 2 pointer solution
            # Sort the nums list
            # Create final return list
            # for each number nums[i]:
                # use two pointers (left, right) on the rest of the array
                # move them inward until they meet

        # Solution:
        # nums.sort()
        # result = []

        # for i in range(len(nums)):
        #     # skip duplicate "first numbers"
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue

        #     left, right = i+1, len(nums)-1

        #     while left < right:
        #         total = nums[i] + nums[left] + nums[right]

        #         if total == 0:
        #             result.append([nums[i], nums[left], nums[right]])

        #             # skip duplicate "second numbers"
        #             while left < right and nums[left] == nums[left+1]:
        #                 left += 1
        #             # skip duplicate "third numbers"
        #             while left < right and nums[right] == nums[right-1]:
        #                 right -= 1

        #             # move both pointers
        #             left += 1
        #             right -= 1

        #         elif total < 0:
        #             left += 1  # need bigger sum
        #         else:
        #             right -= 1  # need smaller sum

        # return result

        # ********************

        nums.sort()
        res = []

        for basep in range(len(nums)):
            if basep > 0 and nums[basep] == nums[basep - 1]:
                continue
            
            left, right = (basep + 1), (len(nums) - 1)

            while left < right:
                total = nums[basep] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[basep], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1

                    left += 1
                    right -= 1
                
                elif total > 0:
                    right -= 1
                
                else:
                    left += 1
        
        return res


