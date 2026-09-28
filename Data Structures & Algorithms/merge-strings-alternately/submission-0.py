class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        res = ""
        len1, len2 = len(word1), len(word2)

        while (p1 < len1) and (p2 < len2):
            res = res + word1[p1] + word2[p2]
            p1 += 1
            p2 += 1
        
        if (p1 < len1):
            res += word1[p1 : len1]
        else:
            res += word2[p2 : len2]
        
        return res