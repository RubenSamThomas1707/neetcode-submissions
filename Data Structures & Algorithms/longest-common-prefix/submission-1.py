class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        prefix = ""
        str1, str2 = strs[0], strs[len(strs) - 1]

        for i in range(len(str1)):
            if str1[i] == str2[i]:
                prefix += str1[i]
            else:
                break
        return prefix