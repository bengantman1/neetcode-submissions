class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = sorted(zip(position, speed), reverse=True) # (highest pos, speed), ...
        #print(data)
        highTime = 0
        prevTime = 0
        fleets = 1
        for i, (pos, spd) in enumerate(data):
            time = (target - pos) / spd
            if i == 0:
                prevTime = time
                highTime = time
            else:
                if time > highTime and time > prevTime:
                    fleets += 1
                highTime = max(highTime, time)
                prevTime = time
            #print(f'time: {time}, highTime: {highTime}, prevTime: {prevTime}')
            #print(fleets)
        
        return fleets




