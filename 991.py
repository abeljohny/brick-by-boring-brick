class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ops = 0
        while target > startValue:
            ops += 1
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
        return ops + (startValue - target)


# print(Solution().brokenCalc(2, 3))
# print(Solution().brokenCalc(5, 8))
# print(Solution().brokenCalc(3, 10))
