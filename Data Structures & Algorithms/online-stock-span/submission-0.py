class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        # Brute Force:
            # days = 1
            # n = len(self.prices) - 1

            # while n >= 0 and self.prices[n] <= price:
            #     days += 1
            #     n -= 1
            
            # self.prices.append(price)
            # return days
        
        days = 1
        while self.prices and self.prices[-1][0] <= price:
            days += self.prices[-1][1]
            self.prices.pop()
        
        self.prices.append((price, days))
        return days
        

            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)