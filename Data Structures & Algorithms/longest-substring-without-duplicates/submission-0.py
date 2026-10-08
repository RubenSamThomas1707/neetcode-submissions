class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 2 Pointer / Sliding window approach:
            # Check if string is empty
                # Yes, then return 0
            # Initialize start and next
            # Initialize maxLength = 1
            # Iterate through the string s where next < len(s)
                # If ord(s[next]) - ord(s[next-1]) == 1:
                    # increment next by 1
                # else
                    # maxLength = max((next-start), maxLength)
                    # start=next
                    # next=next+1
            # Return the maxLength
        
        # Solution (Doesnt work completely for the test case "au"):
        # if not s:
        #     return 0

        # startIndex, nextIndex, maxLength = 0, 1, 1
        # while nextIndex < len(s):
        #     print(f"Current Char: {s[nextIndex - 1]}")
        #     print(f"Next Char: {s[nextIndex]}")
        #     print("________________")
        #     if (ord(s[nextIndex]) -  ord(s[nextIndex - 1]) >= 0):
        #         nextIndex += 1
        #     else:
        #         maxLength = max((nextIndex-startIndex), maxLength)
        #         startIndex = nextIndex
        #         nextIndex += 1
        
        # return maxLength

        # Chatgpt solution:
        # if not s:
        #     return 0

        # seen = set()  # to store unique characters in the window
        # left = 0
        # max_len = 0

        # for right in range(len(s)):
        #     while s[right] in seen:
        #         # remove from the left until duplicate is gone
        #         seen.remove(s[left])
        #         left += 1
        #     seen.add(s[right])
        #     max_len = max(max_len, right - left + 1)

        # return max_len

        #-----------------

        seen = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            # Only shrink window if the duplicate character is within current window bounds
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            
            seen[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len


