class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Previous Approach
            # if len(tokens) < 3:
            #     return int(tokens[0])

            # lst = []
            # for t in tokens:
            #     if not (t == '+' or t == '-' or t == '*' or t == '/'):
            #         lst.append(t)
            #     else:
            #         if t == '+':
            #             res = (int(lst[-2]) + int(lst[-1]))
            #         elif t == '-':
            #             res = (int(lst[-2]) - int(lst[-1]))
            #         elif t == '*':
            #             res = (int(lst[-2]) * int(lst[-1]))
            #         elif t == '/':
            #             res = int(int(lst[-2]) / int(lst[-1]))
            #         lst.pop()
            #         lst.pop()
            #         lst.append(res)
            # return lst[0]
        
        stack = []

        for token in tokens:
            if token == "+":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(num1 + num2)
            elif token == "-":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(num1 - num2)
            elif token == "*":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(num1 * num2)
            elif token == "/":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(int(num1 / num2))
            else:
                stack.append(int(token))
        
        return stack[0]