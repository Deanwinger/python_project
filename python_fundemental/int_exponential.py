'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''

'''
需要注意的地方:
当指数为负数的时候
当底数为零切指数为负数的情况
在判断底数base是不是等于0的时候,不能直接写base==0, 因为计算机内表示小数时有误差,只能判断他们的差的绝对值是不是在一个很小的范围内
'''

'''
当n为偶数, a^n = a^(n/2) * a^(n/2)
当n为奇数, a^n = a^((n-1)/2) * a^((n-1)/2)) * a
利用右移一位运算代替除以2(类似于整除//)
利用位与运算代替了求余运算法%来判断一个数是奇数还是偶数
优化代码速度
'''
#leetcode 题50
#题11

class Solution(object):
    def Power(self, base, exponential):
        if base == 0:
            if exponential == 0:
                raise Exception("没有意义")
            else:
                return 0
        
        if exponential == 0:
            return 1
        if exponential == 1:
            return base
        if exponential == -1:
            return 1/base
        
        result = self.Power(base, exponential>>1)
        result *= result
        if exponential%2 == 1:
            result *= base 
        return result