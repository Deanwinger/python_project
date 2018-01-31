'''
统计一个数字在排序数组中出现的次数。
'''

#题38
#leetcode 类似题34. Search for a Range

class Solution:
    def GetNumberOfK(self, data, k):
        start = 0
        end = len(data) - 1
        mid = (start + end) // 2
        if data[mid] > k:
            pass
        elif data[mid] < k:
            pass
        else data[mid] == k:
            self.GetFirstK()
            self.GetLastK()

    def GetFirstK(self, data, length, k, start, end):
        pass

    def GetLastK(self, data, length, k, start, end):
        pass