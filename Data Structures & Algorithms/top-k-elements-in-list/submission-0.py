class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Initialize the final list
        # Step 2: Iterate through the nums list
            # Check if value exists in seen hashmap (key = num, val = count)
                # If exists
                    # Increment the count
                # Else
                    # Create new entry in hashmap to add the value
        # Step 3: Sort the hashmap from descending to ascending
        # Step 4: Return the top k elements

        # res = []
        # seen = defaultdict(int)
        # for num in nums:
        #     seen[num] += 1
        # sorted_items = sorted(seen.items(), key=lambda x: x[1], reverse=True)
        # res = [num for num, count in sorted_items[:k]]
        # return res
            
        
        # Neetcode Solution:
        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)

        # arr = []
        # for num, cnt in count.items():
        #     arr.append([cnt, num])
        # arr.sort()

        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        # return res

        # Bucket Sort Method:
        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        # for num, cnt in count.items():
        #     freq[cnt].append(num)

        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res
        
        #####################################
        #####################################

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        freqList = [[] for _ in range(len(nums) + 1)]

        for key, value in freq.items():
            freqList[value].append(key)
        
        finalList = []

        for i in range(len(nums), -1, -1):
            lst = freqList[i]
            for num in lst:
                if len(finalList) == k:
                    return finalList
                finalList.append(num)
        return finalList
