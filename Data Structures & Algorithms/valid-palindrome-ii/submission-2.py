class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # Call helper method to check the two remaining index ranges:
                # 1. Skip left character: check s from l + 1 to r
                # 2. Skip right character: check s from l to r - 1
                return self.isPalindromeRange(s, l + 1, r) or self.isPalindromeRange(s, l, r - 1)
            
            l += 1
            r -= 1

        return True

    # Helper method to check if s[i...j] is a valid palindrome in-place
    def isPalindromeRange(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True