# leetcode 64. Minimum Path Sum (Medium)

# 程序员代码面试指南 P187

# 2019-5-14 非常经典的动态规划, 下面的答案还可以进行空间优化, to be finished

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        if not row:
            return 0
        
        col = len(grid[0])
        if not col:
            return 0
        
        dp = [[0]*col for _ in range(row)]
        sum = 0
        for i in range(row):
            sum += grid[i][0]
            dp[i][0] = sum
            
        sum = 0            
        for j in range(col):
            sum +=  grid[0][j]
            dp[0][j] = sum
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
                
        return dp[row-1][col-1]
            

if __name__ == "__main__":
    a = [[1,3,1],[1,5,1],[4,2,1]]
    s = Solution()
    print(s.minPathSum(a))