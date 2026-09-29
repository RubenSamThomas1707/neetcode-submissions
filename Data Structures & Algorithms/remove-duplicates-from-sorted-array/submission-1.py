class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        pointer = 0

        for i in range(len(nums)):
            val = nums[i]
            if val not in seen:
                nums[pointer] = val
                seen.add(val)
                pointer += 1

        return pointer