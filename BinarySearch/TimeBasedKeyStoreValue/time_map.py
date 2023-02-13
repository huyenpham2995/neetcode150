class TimeMap:

    def __init__(self):
        # dictionary that is sorted by ascending order of timestamp.
        # we don't have to sort it, since the timestamp of the next item inserted is bigger than the last one in the dict.
        self._time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._time_map.keys():
            self._time_map[key] = [(value,timestamp)]
        else:
            self._time_map[key].append((value,timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self._time_map.keys():
            return ""
        else:
            l, r = 0, len(self._time_map[key]) -1
            max_timestamp = float("-inf")
            res = ""

            while l <= r:
                mid = (l+r)//2
                if self._time_map[key][mid][1] <= timestamp:
                    if max_timestamp < self._time_map[key][mid][1]:
                        max_timestamp = self._time_map[key][mid][1]
                        res = self._time_map[key][mid][0]
                    l = mid+1
                else:
                    r = mid-1
            return res
