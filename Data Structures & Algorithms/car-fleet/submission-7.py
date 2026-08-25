class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = sorted(zip(position, speed), reverse=True) # (highest pos, speed), ...
        pos0, spd0 = data[0]
        prevTime = (target - pos0) /spd0
        fleets = 1
        for i in range(1, len(data)):
            pos, spd = data[i]
            time = (target - pos) / spd
            
            if time > prevTime:
                fleets += 1
                prevTime = time # only update if you come across a time that is bigger. prevTime will hold largest time so far

            #print(f'time: {time}, prevTime: {prevTime}')
            #print(fleets)
        
        return fleets




