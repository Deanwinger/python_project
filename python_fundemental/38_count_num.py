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