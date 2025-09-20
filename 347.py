from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Counter
        frequency_map = Counter(nums)
        top_k = frequency_map.most_common(k)
        return [elem[0] for elem in top_k]

        # # Min-Heap
        # frequency_map = Counter(nums)
        # min_heap = []
        # for elem, freq in frequency_map.items():
        #     heapq.heappush(min_heap, (freq, elem))
        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)
        # return [elem[1] for elem in min_heap]