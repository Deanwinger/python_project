# leetcode 78.Subsets (Medium)
# leetcode 90. Subsets II (Medium)


# leetcode 78. 子集
# 2019-7-6 完美, 经典回溯, 我是通过基础case, 倒推出来的, 最后肯定是返回[[]], 
# 需要保存这个基础变量, 同时要把每次返回的值, 都加上当前的[nums[0]]
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        n = len(nums)
        rec = []
        
        res = self.subsets(nums[1:])

        for r in res:
            rec.append(r)
            rec.append([nums[0]]+r)
        return rec

# leetcode 90
# 2019-7-6 愚蠢, 肯定有更好的方法, to be finished...
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        rec = self.get_sub(nums)
        ret = []
        res = [sorted(r) for r in rec]
        print(res)
        for i in res:
            if i not in ret:
                ret.append(i)
        return ret
        
        
    def get_sub(self, nums):
        if not nums:
            return [[]]
        
        rec = []
        res = self.get_sub(nums[1:])
        for r in res:
            rec.append(r)
            t = [nums[0]]+r
            rec.append(t)
        return rec
        


if __name__ == "__main__":
    a = [1,2,3]
    s = Solution()
    print(s.subsets(a))