class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
       # Previous Approach
        # res = [0] * len(temperatures)
        #     stack = []  # pair: [temp, index]

        #     for i, t in enumerate(temperatures):
        #         while stack and t > stack[-1][0]:
        #             stackT, stackInd = stack.pop()
        #             res[stackInd] = i - stackInd
        #         stack.append((t, i))
        #     return res

        res, stack = [0] * len(temperatures), []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            
            stack.append((temp, i))
        
        return res