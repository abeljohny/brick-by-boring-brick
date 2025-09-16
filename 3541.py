from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        s_count = Counter(s)
        vowels = max([s_count[ch] for ch in s_count if ch in 'aeiou'], default=0)
        consonants = max([s_count[ch] for ch in s_count if ch not in 'aeiou'], default=0)
        return vowels + consonants
