class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = defaultdict(int)

        for num in nums:
            print(num)
            freq[num] += 1
        
        index = 0

        for i in range(freq[0]):
            nums[index] = 0
            index += 1
        
        for i in range(freq[1]):
            nums[index] = 1
            index += 1
        
        for i in range(freq[2]):
            nums[index] = 2
            index += 1

        