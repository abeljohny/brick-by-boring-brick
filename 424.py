from collections import  defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        l = 0
        max_freq = 0
        max_length = 0

        for r in range(len(s)):
            char_freq[s[r]] += 1
            max_freq = max(max_freq, char_freq[s[r]])

            window_length = r - l + 1
            if window_length - max_freq > k:
                char_freq[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)

        return max_length