# leetcode 217：Contains Duplicate 
# leetcode 219：Contains Duplicate II 
# leetcode 220：Contains Duplicate III 
# leetcode 287：Find the Duplicate Number

# 剑指offer(2) 题3, 可以好好玩味一下
# 2019-7-13 leetcode 287 to be finished, 空间复杂度为O(n), 题目要求是O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return
        
        n = len(nums)
        rec=[0]*(n+1)
        for i in range(n):
            rec[nums[i]] += 1
            
        for i in range(n+1):
            if rec[i]>1:
                return i