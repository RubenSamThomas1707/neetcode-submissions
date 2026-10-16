class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 1:
            return 1
        
        people = sorted(people)

        l, r = 0, len(people) - 1
        minBoats = 0

        while l <= r:
            if l == r:
                minBoats += 1
                break 
            
            if (people[r] + people[l] <= limit):
                l += 1
            
            minBoats += 1
            r -= 1

        return minBoats