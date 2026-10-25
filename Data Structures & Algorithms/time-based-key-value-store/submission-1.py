class TimeMap:

    # Wrong approach
        # def __init__(self):
        #     self.store = defaultdict(dict)

        # def set(self, key: str, value: str, timestamp: int) -> None:
        #     self.store[key][timestamp] = value
        #     print(self.store) 

        # def get(self, key: str, timestamp: int) -> str:
        #     values = self.store[key]

        #     print(len(values))
        #     print(f"{values = }")

        #     if len(values) == 0:
        #         return "" 
        #     elif values.get(timestamp, "") != "":
        #         return values[timestamp]  

        #     minTimestamp, maxTimestamp = 0, timestamp
        #     res = ""

        #     while minTimestamp <= maxTimestamp:
        #         middle = minTimestamp + (maxTimestamp - minTimestamp) // 2

        #         val = values.get(middle, "")

        #         if val != "":
        #             res = val
        #             minTimestamp = middle + 1
        #         else:
        #             maxTimestamp = middle - 1
            
        #     return res

    def __init__(self):
        # Maps a key to a list of tuples: [(timestamp1, value1), (timestamp2, value2), ...]
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
            
        values = self.store[key]
        
        # Binary search over the list indices
        left, right = 0, len(values) - 1
        res = ""
        
        while left <= right:
            middle = left + (right - left) // 2
            curr_timestamp, curr_value = values[middle]
            
            # If the recorded timestamp is less than or equal to our target,
            # it's a valid candidate. Let's record it and look for a closer (larger) one on the right.
            if curr_timestamp <= timestamp:
                res = curr_value
                left = middle + 1
            else:
                # Too recent, search the left half
                right = middle - 1
                
        return res

