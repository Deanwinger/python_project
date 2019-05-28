# leetcode 51. N-Queens, 52. N-Queens II


'''
三个要素:
choice, 意味着新一轮递归(recursion represents decisions)
restrain: choice之前的约束

goal: 目标, 退出标志

'''

# 2019-5-28 程序员代码面试指南 P239, 这里虽然用到了递归, 但是貌似没有很多人都提到的回溯法, 
# 回溯法 to be finished
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
        
if __name__ == "__main__":
    n = 8
    s = Solution()
    print(s.totalNQueens(n))