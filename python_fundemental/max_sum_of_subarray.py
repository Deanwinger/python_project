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
        nCurSum = 0
        nGreatestSum = array[0]
        for i in range(len(array)):
            if nCurSum <= 0:
                nCurSum = array[i]
            else:
                nCurSum += array[i]

            if nCurSum > nGreatestSum:
                nGreatestSum = nCurSum

        return nGreatestSum
    


class Solution(object):
    def maxSubArray(self, nums):
        """
        有思路之后很简单
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        
        max_sum = nums[0]
        cur_sum = 0
        length = len(nums)
        i = 0
        while i < length:
            cur_sum += nums[i]
            
            if cur_sum > max_sum:
                max_sum = cur_sum
            
            if cur_sum < 0:
                cur_sum = 0
            i += 1
        return max_sum


# 类似题leetcode 674. Longest Continuous Increasing Subsequence
class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        length = len(nums)
        rec = 1
        max_rec = 1
        cur = nums[0]
        for i in range(1, length):
            if nums[i] > cur:
                rec +=1
            else:
                rec = 1
            
            if rec > max_rec:
                max_rec = rec
            cur = nums[i]
        return max_rec



if __name__=='__main__':
    array = [-2,1,-3,4,-1,2,1,-5,4]
    # array = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    # array = [1, -2, 3, 10, -4, 7, 2, -5]
    s = Solution()
    print(s.maxSum(array))
