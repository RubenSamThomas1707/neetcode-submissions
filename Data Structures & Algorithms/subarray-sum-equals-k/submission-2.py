class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # # Brute Force Solution: O(N^2)
        # total = 0

        # for i in range(len(nums)):
        #     totalSum = 0
        #     for j in range(i, len(nums)):
        #         # print(f"{i = } : {j = }")
        #         totalSum += nums[j]
        #         # print(f"{totalSum = }")
        #         if totalSum == k:
        #             total += 1
            
        #         # print(total)
        #     # print("****")

        # return total

        # *********

        res = curSum = 0
        prefixSums = { 0 : 1 }

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res