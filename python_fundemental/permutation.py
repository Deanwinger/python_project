"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
结果请按字母顺序输出。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
"""

# 题28



# leetcode 46. Permutations

class Solution:
    def permute(self, nums):
        """
        leetcode 46 题题解
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        if len(nums) == 1:
            return [nums]
        
        n = len(nums)
        rec = []
        for i in range(n):
            res = self.permute(nums[:i] + nums[i+1:])
            for r in res:
                a = [nums[i]] + r
                rec.append(a)
        return rec

    def permuteUnique(self, nums):
        """
        leetcode 47. Permutations II, 同题28
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        rec = self.permute(nums)
        for r in rec:
            if r in res:
                continue
            res.append(r)
        return res
    