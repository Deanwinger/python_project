# leetcode 718. 最长重复子数组
# # 剑指offer(2) 题 48 最长不包含重复字符的子串

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

# 2019-7-6 O(1)空间优化完成
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n1 = len(A)
        n2 = len(B)
        
        row = 0
        col = n2-1
        
        cur = 0
        while row < n1:
            i = row
            j = col
            res = 0
            while i < n1 and j < n2:
                if A[i] == B[j]:
                    res += 1
                else:
                    res = 0
                    
                if res > cur:
                    cur = res
                i += 1
                j += 1

            if col > 0:
                col -= 1
            else:
                row += 1
        return cur