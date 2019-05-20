# 题 48
# leetcode 5. Longest Palindromic Substring
# 讲解 https://www.felix021.com/blog/read.php?2040 Manacher's ALGORITHM



# 靠, leetcode 上面提示超出時間限制, 程序是沒有問題的
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        n = len(s)
        dp = [[False]*n for i in range(n)]
        
        # initiate
        for i in range(n):
            dp[i][i] = True
        
        first = last = 0
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                if dp[i][i+1]:
                    first = i
                    last = i+1

        
        # 有点混乱, 此处i代表长度, j代表行(前一个指针)
        for i in range(3, n+1):
            for j in range(n):
                if i+j<=n:
                    # i+j-1 代表后一个指针
                    if s[i+j-1] == s[j]:
                        dp[j][i+j-1] = dp[j][i+j-1] or dp[j+1][i+j-2]
                        if dp[j][i+j-1]:
                            first = j
                            last = i+j-1

        return s[first:last+1]

if __name__ == "__main__":
    s = "caba"
    print(len(s))
    solu = Solution()
    print(solu.longestPalindrome(s))


