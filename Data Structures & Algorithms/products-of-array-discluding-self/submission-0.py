class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force approach
        # Create list to return final value
        # Iterate over nums array
            # Create variable to store product and initialize it to 1
            # Iterate over nums array again
                # Check if current != index,
                    # Calculate product
            # Append product to list
        # Return list
        # -------------------------------------
        # res = []
        # for i1 in range(len(nums)):
        #     product = 1
        #     for i2, num2 in enumerate(nums):
        #         if i1 != i2:
        #             product *= num2
        #     res.append(product)
        # return res


        # -------------------------------------
        # 1 - 48 (2 x 4 x 6)
        # 2 - 24 (1 x 4 x 6)
        # 4 - 12 (1 x 2 x 6)
        # 6 - 8 (1 x 2 x 4)
        # Pseudocode - Storing prefix and suffix
        # Create prefix list (len(nums))
        # Prefix[0] = 1
        # Iterate through nums list using range index+1 start
            # Prefix[index] = Prefix[index-1] * nums[index-1]
        
        # Create suffix list(len(nums))
        # Suffix[len(nums) - 1] = 1
        # Iterate through the nums list from other end (len(nums) - 2)
            # Suffix[index] = Suffix[index+1] * nums[index+1]
        
        # Instantiate res list
        # Iterate based on len of suffix or prefix
            # Calcualte product and store in each index
        # Return res
        # -------------------------------------
        # prefix = [1] * len(nums)
        # for idx in range(1, len(nums)):
        #     prefix[idx] = prefix[idx-1] * nums[idx-1]
        
        # suffix = [1] * len(nums)
        # for idx in range(len(nums)-2, -1, -1):
        #     suffix[idx] = suffix[idx+1] * nums[idx+1]
        
        # res = []
        # for idx in range(len(prefix)):
        #     res.append(prefix[idx] * suffix[idx])
        # return res

        n = len(nums)

        leftProd = [1] * n
        rightProd = [1] * n
        res = [1] * n

        for i in range(1, n):
            leftProd[i] = leftProd[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            rightProd[i] = rightProd[i+1] * nums[i+1]

        for i in range(n):
            res[i] = leftProd[i] * rightProd[i]

        return res




