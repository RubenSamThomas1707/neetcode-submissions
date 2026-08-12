class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        maxFreq, maxFreqNumber = 0, -1

        for k, v in freq.items():
            if v > maxFreq:
                maxFreq = v
                maxFreqNumber = k

        return maxFreqNumber