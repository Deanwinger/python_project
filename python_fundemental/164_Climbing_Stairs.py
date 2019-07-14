# leetcode 70. Climbing Stairs (Easy)
# 动态规划的题目基本上从此题开始

class Solution:
    def climbStairs(self, n: int) -> int:
        '''最直观的解法, 但是会超出时间限制'''
        if n == 1 :
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs_v1(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        starter = [1,2]
        i = 3
        while i <= n:
            starter[(i-1)%2] = starter[0] + starter[1]
            i += 1
        return starter[(n-1)%2]