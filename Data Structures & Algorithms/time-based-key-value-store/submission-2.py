class TimeMap:

    def __init__(self):
        self.map = {} # key : [[values], [timestamps]]



    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key][0].append(value)
            self.map[key][1].append(timestamp)
        else:
            self.map[key] = [[value], [timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        vals = self.map[key][0]
        times = self.map[key][1]

        l = 0
        r = len(times) - 1

        while l <= r:
            m = (l + r) // 2
            if times[m] == timestamp:
                return vals[m]
            if timestamp > times[m]:
                l = m + 1
            else:
                r = m - 1
        if times[l - 1] > timestamp:
            return ""
        return vals[l - 1]



