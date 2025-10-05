class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        revisions1 = version1.split('.')
        revisions2 = version2.split('.')
        max_len = max(len(revisions1), len(revisions2))
        while len(revisions1) < max_len:
            revisions1.append('0')
        while len(revisions2) < max_len:
            revisions2.append('0')
        for i in range(max_len):
            n1, n2 = int(revisions1[i]), int(revisions2[i])
            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1
        return 0


# print(Solution().compareVersion("1.2", "1.10"))
# print(Solution().compareVersion("1.01", "1.001"))
# print(Solution().compareVersion("1.0", "1.0.0.0"))
