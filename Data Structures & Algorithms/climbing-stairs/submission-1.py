class Solution:
    def climbStairs(self, n: int) -> int:
        # O(N) space using array:
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        
        # stairs = [0] * n
        # stairs[0], stairs[1] = 1, 2

        # for i in range(2, n):
        #     stairs[i] = stairs[i-1] + stairs[i-2]
        
        # return stairs[n-1]

        # ---------
        # Optimization: O(1) Space:
        if n <= 2:
            return n

        prev2 = 1
        prev1 = 2
        
        current = 0
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return current