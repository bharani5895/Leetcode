class Solution:
    def longestcs(self, s1: str, s2: str, i: int, j: int, dp: list[list[int]]) -> int:
        if i == len(s1) or j == len(s2):
            return 0
        if dp[i][j] != -1:
            return dp[i][j]

        if s1[i] == s2[j]:
            dp[i][j] = 1 + self.longestcs(s1, s2, i + 1, j + 1, dp)
        else:
            case1 = self.longestcs(s1, s2, i, j + 1, dp)
            case2 = self.longestcs(s1, s2, i + 1, j, dp)
            dp[i][j] = max(case1, case2)
            
        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[-1] * m for _ in range(n)]
        return self.longestcs(text1, text2, 0, 0, dp)