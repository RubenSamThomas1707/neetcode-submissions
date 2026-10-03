class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute Force Approach:
            # Initialize max = 0
            # Iterate over heights list for i in range len(heights) - 1
                # For j in range from i+1 to len(heights)
                # startHeight = height[i]
                # endHeight = height[j]
                # Check if startHeight and endHeight is not 0:
                    # k = min(startHeight or endHeight)
                    # storedWater = k * (j-i)
                    # if storedWater > max:
                        # max = storedWater
            # return max
        
        # Solution: O(N^2)
        # res = 0
        # for i in range(len(heights) - 1):
        #     for j in range(i+1, len(heights)):
        #         startHeight = heights[i]
        #         endHeight = heights[j]
        #         if startHeight != 0 and endHeight != 0:
        #             k = min(startHeight, endHeight)
        #             storedWater = k*(j-i)
        #             res = max(storedWater, res)
        # return res

        # --------------------------------------------------

        # More optimal solution?:
            # Initialize result = 0
            # Initialize 2 pointers
                # start = 0
                # end = len(heights)
            # While start < end
                # result = max(result, min(heights[start], heights[end]) * (end-start))
                # If heights[start] < heights[end]:
                    # start += 1
                # Else:
                    # end -= 1
            # return result
        
        # Solution: O(N)
        # result, start, end = 0, 0, len(heights)-1
        # while start < end:
        #     result = max(result, (min(heights[start], heights[end]) * (end-start)))
        #     if heights[start] < heights[end]:
        #         start += 1
        #     else:
        #         end -= 1
        # return result

        # ------------------------------

        l, r = 0, len(heights) - 1
        maxWater = 0

        while l < r:
            water = (
                min(heights[l], heights[r]) * (r - l)
            )
            maxWater = max(water, maxWater)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater




