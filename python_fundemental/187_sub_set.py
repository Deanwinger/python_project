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


if __name__ == "__main__":
    a = [1,2,3]
    s = Solution()
    print(s.subsets(a))


[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [], [1], [3], [1, 3], [], [2], [3], [2, 3],[], [3]]