'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
1~13中包含1的数字有1、10、11、12、13因此共出现6次。
'''
from datetime import datetime

# leetcode 233. Number of Digit One
# 题32

class Solution:
    def countDigitOne(self, n):
        """
        这个方法能行，但是效率非常低
        :type n: int
        :rtype: int
        """
        result = 0
        t1 = datetime.now()
        for num in range(1, n+1):
            r = self.get_ones(num)
            result += r
        t2 = datetime.now()
        print("total time is: %s", t2-t1)
        return result
    
    def get_ones(self, n):
        c = 0
        while n:
            if (n % 10) == 1:
                c += 1
            n = n // 10
        return c

if __name__ == "__main__":
    s = Solution()
    print(s.countDigitOne(3184191))
