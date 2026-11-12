class Solution:
    def simplifyPath(self, path: str) -> str:
        pathBreakdown = path.split('/')
        stack = []

        for p in pathBreakdown:
            if p != '' and p != '.':
                if p == '..':
                    if stack:
                        stack.pop()
                    else:
                        continue
                else:
                    stack.append(p)
        
        if len(stack) == 0:
            return "/"

        res = ""
        while stack:
            res = "/" + stack.pop() + res

        return res