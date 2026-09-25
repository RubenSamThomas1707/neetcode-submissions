class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0

        for i in range(1, len(prices)):
            print(f"{totalProfit = }")
            if prices[i-1] < prices[i]:
                print(f"{prices[i-1] = }")
                print(f"{prices[i] = }")
                totalProfit += (prices[i] - prices[i-1])

            print("***")
        
        return totalProfit