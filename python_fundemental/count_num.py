'''
统计一个数字在排序数组中出现的次数。
'''

#题38
#leetcode 类似题34. Search for a Range

class Solution:
    def GetNumberOfK(self, data, k):
        if not data:
            return
        number = 0
        start = 0
        end = len(data) - 1 
        first = self.GetFirstK(data, k, start, end)
        last = self.GetLastK(data, k, start, end)
        if first > -1:
                number = last - first + 1
        return number

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
            end = mid - 1
        else:
            start = mid + 1
        return self.GetFirstK(data, k, start, end)

    def GetLastK(self, data, k, start, end):
        mid = (start + end) // 2
        if data[mid] == k:
            if mid < end and data[mid+1] == k:
                start = mid + 1
            else:
                return mid
        elif data[mid] > k:
            end = mid - 1
        else:
            start = mid + 1
        return self.GetLastK(data, k, start, end)

if __name__=='__main__':
    alist = [3,3,3,3,4,5]
    s = Solution()
    print(s.GetNumberOfK(alist, 3))