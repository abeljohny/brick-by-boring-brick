from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            s_count = Counter(s)
            anagrams[tuple(sorted(s_count.items()))].append(s)
        return list(anagrams.values())