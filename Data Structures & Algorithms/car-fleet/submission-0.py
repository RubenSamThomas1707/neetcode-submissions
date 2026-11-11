class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Bucket approach to bucket cars with same speed together
        # Invalid approach since slower cars can block/combine into single fleet
            # buckets = defaultdict(int)

            # for p, s in zip(position, speed):
            #     # print(f"{buckets = }")
            #     res = math.ceil((target - p) / s)
            #     # print(f"{p = } | {s = } | {res = }")
            #     buckets[res] += 1

            # fleet = 0
            # for count in buckets:
            #     if count > 0:
            #         fleet += 1

            # return fleet
        
        # Approach 2:
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        current_fleet_time = 0
        
        for p, s in cars:
            time_to_target = (target - p) / s
            
            # If the current car takes MORE time than the fleet ahead of it,
            # it cannot catch up to them, so it forms a new fleet.
            if time_to_target > current_fleet_time:
                fleets += 1
                current_fleet_time = time_to_target
                
        return fleets