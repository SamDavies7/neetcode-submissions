class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        unobstructedTimes = [-1] * len(position)
        for i in range(len(position)):
            unobstructedTimes[i] = (target - position[i]) / speed[i]
        cars = sorted(zip(position, unobstructedTimes), reverse=True)
        fleets = 0
        lead = 0  
        for _, t in cars:
            if t > lead:    
                fleets += 1
                lead = t
        return fleets
