import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        maxHeap = []
        res = []

        for i in range(k):
            heapq.heappush(maxHeap, (-nums[i], i))
        
        # print(f"{maxHeap = }")
        
        res.append(-maxHeap[0][0])
        # print(f"{res = }")

        for i in range(k, len(nums)):
            heapq.heappush(maxHeap, (-nums[i], i))
            left += 1

            while maxHeap[0][1] < left:
                heapq.heappop(maxHeap)
            
            # print(f"{maxHeap = }")
            res.append(-maxHeap[0][0])
            # print(f"{res = }")
            # print("********")

        return res