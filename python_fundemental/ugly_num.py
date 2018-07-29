'''
把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''

# 题34

# leetcode 263. Ugly Number
# leetcode 264. Ugly Number II 同本题

class Solution:
    def is_ugly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # if num == 0:
        #     return False

        while num % 2 == 0:
            num /= 2

        while num % 3 == 0:
            num /= 3

        while num % 5 == 0:
            num /= 5
        return num == 1
    
    def ugly_num(self, N):
        count = 0
        rec = []
        for i in range(1, n):
            if self.is_ugly(i):
                rec.append(i)
                count += 1
        print(count)
        return rec

class Solution(object):
    def nthUglyNumber(self, n):
        """
        题34 的三指针解答, good one
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]