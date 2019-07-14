# leetcode 322. Coin Change (Medium)
# leetcode 518. Coin Change 2 (Medium)
# 0-1 背包问题


# 动态规划 资源
# https://www.geeksforgeeks.org/category/dynamic-programming/

# 322
# 程序员面试指南 P192, 解释的非常清楚, 可以优化, to be finished
class Solution:
    def coinChange(self, coins, amount) -> int:
        n = len(coins)
        dd = float("inf") 
        dp = [[dd] * (amount+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0
        
        for j in range(1, amount+1):
            if j-coins[0]>=0:
                # 关键就在这个+1 这里, 证明参看P192, to be finished
                dp[1][j] = dp[1][j-coins[0]]+1

        for i in range(1, n+1):
            for j in range(1, amount+1):
                if j>=coins[i-1]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]]+1)
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][amount] if dp[n][amount] != dd else -1


# 322 空间优化后的版本
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if amount == 0:
            return 0
        
        if not coins:
            return -1
        
        dd = float("inf")
        col = amount+1
        row = len(coins)
        
        dp = [dd for _ in range(col)]
        dp[0] = 0
        for i in range(row):
            for j in range(col):
                if j >= coins[i]:
                    dp[j] = min(dp[j], dp[j-coins[i]]+1)
                else:
                    dp[j] = dp[j]
        return dp[-1] if dp[-1] != dd else -1

# 518 此版本是正确的,但是超时了
class Solution2:
    def change(self, amount, coins) -> int:
        # if not coins and amount>0:i
        #     return 0

        # if not coins and amount==0:
        #     return 1
        
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = 1
            
        j = 1
        while coins and coins[0]*j <= amount:
            dp[1][coins[0]*j] = 1
            j +=1            
            
        for i in range(1, n+1):
            for j in range(1, amount+1):
                num = 0
                k = 0
                while j-coins[i-1]*k >= 0:
                    num += dp[i-1][j-coins[i-1]*k]
                    k += 1
                dp[i][j] = num
                
        return dp[n][amount]

# 518 优化后的版本, pass 通过
# 优化的关键在于上面的while 循环, 转换成了dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]), 非常elegant, 参考P200
class Solution3:
    def change(self, amount: int, coins) -> int:  
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = 1
            
        j = 1
        while coins and coins[0]*j <= amount:
            dp[1][coins[0]*j] = 1
            j +=1

        print(dp)  
        for i in range(1, n+1):
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j]
                if j-coins[i-1] >=0:
                    dp[i][j] += dp[i][j-coins[i-1]]
        
        print(dp)          
        return dp[n][amount]

# 518 空间优化后的版本, pass 通过
class Solution4:
    def change(self, amount: int, coins) -> int:
        if amount == 0:
            return 1
        if not coins:
            return 0
        
        row = len(coins)
        col = amount+1
        
        dp = [0 for i in range(col)]
        
        # init first row
        for j in range(col):
            if j%coins[0] == 0: 
                dp[j] = 1
                
        print(dp)
        for i in range(1, row):
            for j in range(col):
                if j>=coins[i]:
                    dp[j] = dp[j] + dp[j-coins[i]]

        print(dp)        
        return dp[-1]

if __name__ == "__main__":
    coins = [1,2,5]
    amount = 5
    s = Solution4()
    print(s.change(amount, coins))

