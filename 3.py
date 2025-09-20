class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_set = set()
        l = 0
        max_length = 0

        for r in range(len(s)):
            while s[r] in seen_set:
                seen_set.remove(s[l])
                l += 1
            seen_set.add(s[r])
            max_length = max(max_length, r - l + 1)

        return max_length