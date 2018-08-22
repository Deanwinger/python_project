'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

# 题33 -- to be finished

# leetcode 179. Largest Number, 正好相反

class Solution:
    def smallestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        

from functools import reduce


# leetcode 179, 答案错误， 待调试
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        rec = self.permute(nums)
        return reduce(self.compare, rec)
        
    def permute(self, nums):
        if len(nums) == 1:
            return str(nums[0])
        
        rec = []
        n = len(nums)
        for i in range(n):
            res = self.permute(nums[:i]+nums[i+1:])
            for r in res:
                rec.append(str(nums[i])+r)
        return rec
    
    def compare(self, m, n):
        s = len(m)
        for i in range(s):
            if m[i] > n[i]:
                return m
            elif n[i] > m[i]:
                return  n
            else:
                i += 1

if __name__ == "__main__":
    nums = [3,30,34,5,9]
    s = Solution()
    print(s.largestNumber(nums))