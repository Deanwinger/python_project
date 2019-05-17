# leetcode 718. 最长重复子数组

# 类似题(最长公共子串问题), 程序员代码面试指南P213, 思路完全一致, to be finished(可以进行空间优化)

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        row = len(A)
        col = len(B)
        
        dp = [[0]*(col+1) for _ in range(row+1)]
        for i in range(1, row+1):
            for j in range(1, col+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = 0
                    
        # print(dp)
        maxs = self.get_max_from_matrix(dp)
        return maxs
    
    def get_max_from_matrix(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        maxs = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] > maxs:
                    maxs = matrix[i][j]
        return maxs