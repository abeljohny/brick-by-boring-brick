from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        perms = permutations(digits, r=3)
        output = set()
        for perm in perms:
            if perm[0] != 0 and perm[-1] % 2 == 0:
                digit = perm[0] * 100 + perm[1] * 10 + perm[2]
                output.add(digit)
        return sorted(list(output))