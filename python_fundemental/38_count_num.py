'''
统计一个数字在排序数组中出现的次数。
'''

import traceback
#题38
#leetcode 类似题34. Search for a Range

class Solution:
    def searchRange(self, data, k):
        """
        二分法的应用: 此版的答案好理解的多
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not data:
            return
        start = 0
        end = len(data)-1
        first = self.GetFirstK(data, k, start, end)
        end = self.GetLastK(data, k, start, end)
        return [first, end]
        
    
    def GetFirstK(self, data, k, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if data[mid] == k:
            if mid > 0 and data[mid-1] == k:
                end = mid-1
            else:
                return mid
        elif data[mid] > k:
            end = mid -1
        else:
            start = mid +1
        return self.GetFirstK(data, k, start, end)
    
    def GetLastK(self, data, k, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if data[mid] == k:
            if mid < end and data[mid+1] == k:
                start = mid+1
            else:
                return mid
        elif data[mid] > k:
            end = mid - 1 
        else:
            start = mid + 1
        return self.GetLastK(data, k, start, end)


# 8.23 自己写的, 太多小细节要注意了, 实现的非常不优雅
class Solu(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums)-1
        first = self.find_first(nums, start, end, target)
        last = self.find_last(nums, start, end, target)
        return [first, last]
    
    def find_first(self, nums, start, end, target):
        if end - start == 1 or start == end:
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
            return -1
        
        mid = (start + end) // 2
        if nums[mid] >= target:
            end = mid
        else:
            start = mid
        return self.find_first(nums, start, end, target)
    
    def find_last(self, nums, start, end, target):
        if end - start == 1 or start == end:
            if nums[end] == target:
                return end
            if nums[start] == target:
                return start
            return -1   
        
        mid = (start + end) // 2
        if nums[mid] <= target:
            start = mid
        else:
            end = mid
        return self.find_last(nums, start, end, target)

# 2019-4-15 更加不堪
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        start = 0
        end = len(nums)-1
        first = self.get_first(nums, start, end, target)
        last = self.get_last(nums, start, end, target)
        return [first, last]
    
    def get_first(self, nums, start, end, target):
        if not nums:
            return -1

        # 指向同一个数
        if start == end:
            if nums[start] == target:
                return start
            else:
                return -1
        
        # 两数相邻
        if end-start == 1:
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
            else:
                return -1
            
        # 保证有三个以上元素
        mid = (start+end) // 2
        if nums[mid] == target and nums[mid-1] != target:
            return mid
        
        if nums[mid] == target and nums[mid-1] == target:
            start = self.get_first(nums, start, mid, target)
        elif nums[mid] > target:
            start = self.get_first(nums, start, mid, target)
        else:
            start = self.get_first(nums, mid, end, target)
        return start
        
            
    def get_last(self, nums, start,end, target):
        if not nums:
            return -1

        # 指向同一个数
        if start == end:
            if nums[end] == target:
                return end
            else:
                return -1
        
        # 两数相邻
        if end-start == 1:
            if nums[end] == target:
                return end
            if nums[start] == target:
                return start
            else:
                return -1
        
        # 保证有三个以上元素
        mid = (start+end) // 2
        print(mid)
        if nums[mid] == target and nums[mid+1] != target:
            return mid
        
        if nums[mid] == target and nums[mid+1] == target:
            end = self.get_last(nums, mid, end, target)
        elif nums[mid] > target:
            end = self.get_last(nums, start, mid, target)
        else:
            end = self.get_last(nums, mid, end, target)
        return end


# 2019-6-25 leetcode 34, 这种题目就是常做常新,多做几遍, 很多细节
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        start = 0
        end = len(nums)-1
        first = self.get_first(nums, start, end, target)
        last = self.get_last(nums, start, end, target)
        return [first, last]
    
    def get_first(self, nums, start, end, target):
        if start > end:
            return -1
        
        mid = (start+end)//2
        if nums[mid] == target:
            if (mid>0 and nums[mid-1] != target) or mid ==0:
                return mid
            else:
                end = mid-1
        elif nums[mid] < target:
                start = mid+1
        else:
            end = mid-1
        return self.get_first(nums, start, end, target)
                
                
            
    def get_last(self, nums, start,end, target):
        if start > end:
            return -1
        
        mid = (start+end)//2
        if nums[mid] == target:
            if (mid<end and nums[mid+1] != target) or mid ==end:
                return mid
            else:
                start = mid+1
        elif nums[mid] < target:
                start = mid+1
        else:
            end = mid-1
        return self.get_last(nums, start, end, target)

if __name__=='__main__':
    alist = [1, 8, 8]
    # alist = [5,7,7,8,8,10]
    # alist = [3,3,3,3,4,5]
    # s = Solution()
    s = Solu()
    # print(s.GetNumberOfK(alist, 8))
    # print(s.searchRange(alist, 8))
    # print(s.searchRange(alist, 8))
    print(s.searchRange(alist, 8))