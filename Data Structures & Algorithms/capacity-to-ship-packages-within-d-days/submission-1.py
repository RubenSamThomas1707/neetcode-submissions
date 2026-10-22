class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Brute force solution: O(N * M) where N * M is the value that meets the criteria
        # currWeight = 1

        # while True:
        #     weightLeft = currWeight
        #     totalDays = days

        #     currIndex, totalWeights = 0, len(weights)

        #     while currIndex < totalWeights:
        #         if weights[currIndex] > currWeight:
        #             break
                
        #         if (weightLeft - weights[currIndex]) >= 0:
        #             weightLeft -= weights[currIndex]
        #         else:
        #             totalDays -= 1
        #             weightLeft = currWeight - weights[currIndex]
        #         currIndex += 1
            
        #     totalDays -= 1

        #     if currIndex == totalWeights and totalDays >= 0:
        #         return currWeight
        #     else:
        #         currWeight += 1

        # **********************

        # Binary search approach: O(log (M * N))  M = max of days | N = Number of days

        left = max(weights)
        right = sum(weights)
        res = right
        
        while left <= right:
            capacity = (left + right) // 2
            
            # Simulate shipping with this capacity
            days_needed = 1
            current_load = 0
            
            for w in weights:
                if current_load + w > capacity:
                    days_needed += 1
                    current_load = w
                else:
                    current_load += w
                    
            # Check if this capacity works within the allowed days
            if days_needed <= days:
                res = capacity      # It works, but let's see if a smaller capacity works
                right = capacity - 1
            else:
                left = capacity + 1 # Too small, we need a larger capacity
                
        return res
                

