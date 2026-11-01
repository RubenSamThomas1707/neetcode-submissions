class Solution:
    def isValid(self, s: str) -> bool:
        startParen = ['(', '{', '[']
        endParen = [')', '}', ']']
        lst = []
        for paren in s:
            if paren in startParen:
                lst.insert(0, paren)
            elif paren in endParen:
                if len(lst) == 0: return False
                if (
                    (paren == ')' and lst[0] == '(') or (paren == '}' and lst[0] == '{') or (paren == ']' and lst[0] == '[')
                ):
                    lst.pop(0)
                else:
                    return False
        return len(lst) == 0
