class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for word in word_set:
                l = len(word)
                if i >= l and dp[i - l] and s[i - l:i] == word:
                    dp[i] = True
                    break
        return dp[n]


print(Solution().wordBreak('leetcode', ["leet", "code"]))
