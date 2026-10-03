class TimeMap:

    def __init__(self):
        self.wordMap = collections.defaultdict(list)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.wordMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.wordMap[key]
        l = 0
        r = len(arr) - 1
        ans = ""
        while l <= r:
            mid = (l + r)  // 2
            if  timestamp >= arr[mid][0]:
                ans = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return ans
