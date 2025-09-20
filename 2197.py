class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        def gcd(a, b):
            while b != 0:
                t = b
                b = a % b
                a = t
            return a

        if len(nums) == 1:
            return nums

        i = 0
        while i < len(nums) - 1:
            a, b = nums[i], nums[i + 1]
            if gcd(a, b) > 1:  # non-coprime
                nums.pop(i)
                nums.pop(i)
                nums.insert(i, (a * b) // (gcd(a, b)))
                if i > 0:
                    i -= 1
            else:
                i += 1

        return nums