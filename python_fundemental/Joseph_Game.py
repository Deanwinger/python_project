# 45 题

# leetcode 类似题390. Elimination Game

class Solution:
    def LastRemaining_Solution(self, n, m):
        """数学解法"""
        if n < 1 or m < 1:
            return -1
        remainIndex = 0
        for i in range(1, n+1):
            remainIndex = (remainIndex + m) % i
        return remainIndex

    def LastRemaining(self, n, m):
        """链表解法"""
        pass