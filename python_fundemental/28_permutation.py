"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
结果请按字母顺序输出。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
"""

# 题28
# 此处还有立方体问题， 八皇后问题 to be finished


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
    

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rec = []
        self.permutation(nums, rec)
        return rec

    def permutation(self,  nums, rec):
        if not nums or len(nums) == 1:
            return nums
        
        n = len(nums)
        for i in range(n):
            r = [nums[i]]
            print("r is: ", r)
            print("c is: ", nums[:i]+nums[i+1:])
            print("="*20)
            s = r + self.permutation(nums[:i]+nums[i+1:], rec)
            rec.append(s)
        return 

if __name__ == "__main__":
    nums = [1,2,3]
    s = Solution()
    print(s.permute(nums))