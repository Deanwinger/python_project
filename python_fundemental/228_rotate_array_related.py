# leetcode 153 寻找旋转排序数组中的最小值
# leetcode 33. 搜索旋转排序数组
# leetcode 81. 搜索旋转排序数组 II


#2019-7-7 leetcode 153, 这题已经是滚瓜烂熟了
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        
        if len(nums) == 1:
            return nums[0]
        
        start = 0
        end = len(nums)-1
        
        while True:
            if nums[start] < nums[end]:
                return nums[start]
            if end-start == 1:
                return nums[end]
            
            mid = (start+end)//2
            if nums[mid] < nums[end]:
                end = mid
            if nums[mid] > nums[start]:
                start = mid


# 2019-7-7 leetcode 33 对于这个经典的题目, 我的建议是再做20遍, 很多小细节容易出错
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start = 0
        end = len(nums)-1
        
        # 第一步, 找最小
        ind = self.find_min(nums, start, end)
        
        # 第二步, 二分查找
        l = self.get_target(nums, 0, ind-1, target)
        r = self.get_target(nums, ind, end, target)
        
        res = -1
        if l > -1:
            res= l
        if r > -1:
            res = r
        return res
        
    def find_min(self, nums, start, end):
        if len(nums) == 1:
            return nums[0]
        
        while True:
            if nums[start] < nums[end]:
                return start
            
            if end-start == 1:
                return end
            
            mid = (start+end)//2
            if nums[mid] > nums[start]:
                start = mid
                
            if nums[mid] < nums[end]:
                end = mid

                
    def get_target(self, nums, start, end, target):
        t = nums[start:end+1]
        if not t:
            return -1
        
        if start==end and nums[start]==target:
            return start
        
        while start<=end:
            mid = (start+end)//2
            if nums[mid] > target:
                end = mid-1
            elif nums[mid] < target:
                start = mid+1
            else:
                return mid
        return -1
        
            
        

if __name__ == '__main__':
    s = Solution()
    # nums = [3,1,2]
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(s.search(nums, target))