class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force:
            # Iterate through the prices list
                # Iterate through every price after the current price
                    # Calculate the difference
                    # If currProfit > maxProfit
                        # Update the profit
            # Return profit
        
        # Solution: O(N^2)
        # maxProfit = 0
        # for i in range(len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         maxProfit = max(maxProfit, (prices[j]-prices[i]))
        # return maxProfit

        # ----------------------------
        # More optimal solution?
        # l, r = 0, 1
        # maxP = 0

        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         maxP = max(maxP, profit)
        #     else:
        #         l = r
        #     r += 1
        # return maxP

        # -------------------------------

        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP
        


