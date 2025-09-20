class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        complements = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in complements:
                return complements[complement], idx
            complements[num] = idx
        return []