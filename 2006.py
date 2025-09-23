class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        from collections import Counter
        freq = Counter(nums)
        count = 0
        for num in freq:
            if num + k in freq:
                count += freq[num] * freq[num + k]
        return count

# print(Solution().countKDifference([1,2,2,1], 1))
