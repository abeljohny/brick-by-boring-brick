from heapq import heappush, heappop, heapify
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        h = [-stone for stone in stones]
        heapify(h)
        while len(h) > 1:
            h1, h2 = -heappop(h), -heappop(h)
            r = h1 - h2
            if r > 0:
                heappush(h, -r)
        return -h[0] if h else 0