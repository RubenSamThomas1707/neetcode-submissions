class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Solution:
            # Add elements from nums list to a set (For quick look up)
            # Initialize maxLength = 0
            # Iterate through every num in the set
                # If (currNum - 1) does exists in set (Current number would have to be the start of seq since lower number does not exist)
                    # Set currLength = 1
                    # Add currLength to the current Num (to get the next number) each time and check if it exists in the set
                        # If yes
                            # Increment currLength by 1
                    # maxLength = max(maxLength, currLength)
            # return maxLength

        # ----------------------------

        # numSet = set()
        # maxLength = 0

        # for num in nums:
        #     numSet.add(num)
        
        # for num in numSet:
        #     if (num - 1) not in numSet:
        #         currLength = 1
        #         while (num + currLength) in numSet:
        #             currLength += 1
        #         maxLength = max(maxLength, currLength)
        
        # return maxLength

        # ----------------------------

        elements = set()

        # Adding elements to set for quicker O(1) lookup
        for num in nums:
            elements.add(num)
        
        maxLen = 0

        # Loop through all elements in the list O(N)
        for num in nums:
            # Check if one less than current element not in the list
            # Meaning this would have to be the start for anything greater
            if (num - 1) not in elements:
                currLen = 1
                # Keep on incrementing by 1 till the elements are in the set
                while (num+1) in elements:
                    currLen += 1
                    num += 1
                
                maxLen = max(currLen, maxLen)
        
        return maxLen
            
