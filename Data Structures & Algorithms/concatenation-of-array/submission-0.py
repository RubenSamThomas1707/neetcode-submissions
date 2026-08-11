class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for i in range(2*n):
            res.append(nums[i % n])
        
        print(res)

        return res