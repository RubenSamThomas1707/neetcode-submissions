class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for i, op in enumerate(operations):
            if op == "+":
                scores.append(scores[len(scores)-1] + scores[len(scores)-2])
            elif op == "D":
                scores.append(2 * scores[len(scores)-1])
            elif op == "C":
                scores.pop(-1)
            else:
                scores.append(int(op))
        
        totalScore = 0
        
        for score in scores:
            totalScore += score
        
        return totalScore