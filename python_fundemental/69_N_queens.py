# leetcode 51. N-Queens, 52. N-Queens II
import time

'''
三个要素:
choice, 意味着新一轮递归(recursion represents decisions)
restrain: choice之前的约束

goal: 目标, 退出标志

'''

# 回溯法心得 https://zhuanlan.zhihu.com/p/51882471

# 2019-5-28 程序员代码面试指南 P239
# 位运算 加速 to be finished
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return 0

        rec = [None]*n
        return self.process(0, rec, n)

    def process(self, row, rec, n):
        if row == n:
            return 1

        res = 0
        for col in range(n):
            if self.is_valid(rec, row, col):
                rec[row] = col
                res += self.process(row+1, rec, n)

        return res

    def is_valid(self, rec, row, col):
        for i in range(row):
            if col == rec[i] or (abs(rec[i]-col) == abs(row-i)):
                return False
        return True
        

# 笔记: 3 key
# 1. choice: recursion expresses decision
# 2. constraints
# 3. goal: when to stop
#
#
#
#
#


if __name__ == "__main__":
    n = 12
    t0 = time.time()
    s = Solution()
    print(s.totalNQueens(n))
    t1 = time.time()
    print("time cost: ", t1-t0)