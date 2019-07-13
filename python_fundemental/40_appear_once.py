'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''

# leetcode 260. Single Number III -- 剑指offer 题40
# leetcode 136. Single Number
# leetcode 137. Single Number II -- 剑指offer(2) 题56.2


# 题40 leetcode 260
class Solution:
    def singleNumber(self, nums):
        """
        主要用到了位技巧
        :type nums: List[int]
        :rtype: int
        """
        num1 = 0
        num2 = 0
        result = 0
        for i in nums:
            result ^= i
        indexBit = self.FindFirstBitIs1(result)
        for i in nums:
            res = self.divNums(i, indexBit)
            if res:
                num1 = num1 ^ i
            else:
                num2 = num2 ^ i
        return (num1, num2) 
    
    def FindFirstBitIs1(self, num):
        indexBit = 0
        while num & 1 == 0:
            num = num >> 1
            indexBit += 1
        return indexBit


    def divNums(self, num, indexBit):
        num = num >>indexBit
        if num & 1 == 0:
            return 0
        else:
            return 1
 



if __name__=='__main__':
    nums = [1, 1, 2]
    s = Solution()
    print(s.singleNumber(nums))