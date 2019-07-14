# leetcode 39. 组合总和
# leetcode 40. Combination Sum II (Medium)
# leetcode 216. Combination Sum III (Medium)
# leetcode 377. 组合总和 Ⅳ -- (0-1背包问题)


# leetcode 39
# 2019-7-6, 这个题目请好好揣摩一个最后那个rec.pop()这个动作
class Solution:
    def combinationSum(self, candidates, target):       
        g = []
        rec = []
        nums = sorted(candidates)
        self.get_combo(nums, target, 0, rec=rec, g=g)
        return g
        
    def get_combo(self, nums, target, index, rec=[], g=[]):
        if target == 0:
            g.append(list(rec))
            return 

        if rec and target < rec[-1]:
            return

        for i in range(index, len(nums)):
            rec.append(nums[i])
            self.get_combo(nums, target-nums[i], i, rec=rec, g=g)
            rec.pop()

# leetcode 40
class Solution:
    def combinationSum2(self, candidates, target):
        rec = []
        g = []
        nums = sorted(candidates)
        res = self.get_combi(nums, target)
        return res
    
    def get_combi(self, nums, target):
        if not nums:
            return [[]]
        
        if target == 0:
            return [[]]
        
            
        n = len(nums)
        res = []
        for i in range(n):
            t = nums[i]
            left = nums[:i]+nums[i+1:]
            target -= t
            rec = self.get_combi(left, target)
            for r in rec:
                res.append([nums[i]]+r)
        return res


if __name__ == '__main__':
    candidates = [2, 3, 1]
    target = 5
    # candidates = [10,1,2,7,6,1,5]
    # target = 8
    s = Solution()
    print(s.combinationSum2(candidates, target))