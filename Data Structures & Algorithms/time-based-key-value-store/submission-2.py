class TimeMap:

    def __init__(self):
        self.storage = {} # key = str, list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        vals = self.storage.get(key, [])

        # bs
        l, r = 0, len(vals) - 1

        while l <= r:
            mid = l + (r-l) // 2

            if vals[mid][1] <= timestamp:
                res = vals[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
