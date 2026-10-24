class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Brute force:
        # currRate = 0

        # while True:
        #     currRate += 1
        #     hoursUsed = 0
            
        #     # Simulate total hours needed at this eating rate
        #     for bananas in piles:
        #         # Ceiling division to find hours for this pile
        #         hoursUsed += math.ceil(bananas / currRate)
            
        #     # If Koko can finish all piles within 'h' hours, this rate works!
        #     if hoursUsed <= h:
        #         return currRate

        # ********************

        # Binary search approach
        minRate, maxRate = 1, max(piles)
        finalRate = maxRate

        print(f"{minRate = } | {maxRate = }")

        while minRate <= maxRate:
            currRate = minRate + (maxRate - minRate) // 2
            print(f"{currRate = }")
            hoursUsed = 0

            for pile in piles:
                hoursUsed += math.ceil(pile / currRate)
            
            print(f"Total hours needed at {currRate = } is {hoursUsed}")

            if hoursUsed <= h:
                finalRate = currRate
                maxRate = currRate - 1
            else:
                minRate = currRate + 1
        
        return finalRate