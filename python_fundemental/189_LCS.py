#  最长公共子序列(LCS)
# leetcode 583. 两个字符串的删除操作 基本上就是实现下面的LCS

#  最长公共子串（Longest Common Substring）与最长公共子序列（Longest Common Subsequence）的区别： 
# 子串要求在原字符串中是连续的，而子序列则只需保持相对顺序一致，并不要求连续。
# 例如X = {a, Q, 1, 1}; Y = {a, 1, 1, d, f}那么，{a, 1, 1}是X和Y的最长公共子序列，但不是它们的最长公共字串。
"""
public int lengthOfLCS(int[] nums1, int[] nums2) {
    int n1 = nums1.length, n2 = nums2.length;
    int[][] dp = new int[n1 + 1][n2 + 1];
    for (int i = 1; i <= n1; i++) {
        for (int j = 1; j <= n2; j++) {
            if (nums1[i - 1] == nums2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[n1][n2];
}

"""

# 这只不过是计算出长度, 如何打印出LCS, to be finished
def LCS(s1, s2):
    n1 = len(s1) # 对应行
    n2 = len(s2) # 对应列

    # 我靠, []*n 这个操作是浅拷贝
    # dp=[[0]*(n2+1)]*(n1+1)
    dp = [[0]*(n2+1) for _ in range(n1+1)]
    # print(dp)
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    print(dp)
    return dp[n1][n2]


if __name__ == "__main__":
    s1 = 'sbcnddec'
    s2 = 'scfdeec'
    print(LCS(s1,s2))
