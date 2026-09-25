class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # freq = defaultdict(int)
        # minFreq = len(nums) / 3

        # for num in nums:
        #     freq[num] += 1
        
        # resList = []

        # for key, val in freq.items():
        #     if val > minFreq:
        #         resList.append(key)

        # return resList

        # **********

        freq = defaultdict(int)
        minFreq = len(nums) / 3

        for num in nums:
            freq[num] += 1
        
        resList = set()

        for key, val in freq.items():
            if val > minFreq:
                resList.add(key)

        return list(resList)