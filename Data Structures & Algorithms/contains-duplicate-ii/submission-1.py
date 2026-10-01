class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Pseudocode
        # Initialize a defaultDict with list to store frequencies
        # Loop through nums and check whether key exists,
            # If not then add the element and append its index
            # If it does exist, then loop through the list and try to find the abs value difference
                # If it matches where abs(i-j) <= k, then return True
                # Else append the new index to the list for that number as well
        # Finally return False, since no solutions could be found

        seen = defaultdict(list)

        for idx, val in enumerate(nums):
            prevIndexes = seen.get(val, [])

            for index in prevIndexes:
                if abs(idx - index) <= k:
                    return True
            seen[val].append(idx)
        
        return False