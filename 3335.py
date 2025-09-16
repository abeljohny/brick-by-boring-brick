class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        ch_freq = [0] * 26
        for ch in s:
            ch_freq[ord(ch) - 97] += 1

        mod_val = 10 ** 9 + 7
        for _ in range(t):
            nxt_ch_freq = [0] * 26
            nxt_ch_freq[0] = ch_freq[25]
            nxt_ch_freq[1] = (ch_freq[25] + ch_freq[0]) % mod_val
            for i in range(2, 26):
                nxt_ch_freq[i] = ch_freq[i - 1]
            ch_freq = nxt_ch_freq

        return sum(ch_freq) % mod_val

    # time-expensive:
    # def lengthAfterTransformations(self, s: str, t: int) -> int:
    #     i = 0
    #     while i < t:
    #         j = 0
    #         while j < len(s):
    #             if s[j] == 'z':
    #                 s = s[:j] + 'ab' + s[j+1:]
    #                 j += 1
    #             else:
    #                 s = s[:j] + chr(ord(s[j]) + 1) + s[j+1:]
    #             j += 1
    #         i += 1
    #     return len(s)