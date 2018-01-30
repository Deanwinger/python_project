'''
输入一个整型数组,数组里有整数也有负数。
数组中一二或连续的多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)
'''


#leetcode 53. Maximum Subarray
#题31


class Solution(object):
    def maxSum(self, array):
        if not array:
            return 
        rec_sum = sum = 0
        i = 0
        while i < len(array):
            temp = sum
            sum += array[i]
            if temp < sum:
                rec_sum = sum
            if sum < 0:
                sum = 0
            i += 1
        return rec_sum
            



if __name__=='__main__':
    # array = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    array = [1, -2, 3, 10, -4, 7, 2, -5]
    s = Solution()
    print(s.maxSum(array))
