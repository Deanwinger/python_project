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
        有思路之后很简单, 此题有点微妙, 值得反复玩味;特别是cur_sum, 和max_sum;
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

    # 2019-4-13 重做
    def maxSubArray(self, nums) -> int:
        if not nums:
            return 
        
        cur_sum = nums[0]
        max_sum = cur_sum
        n = len(nums)
        for i in range(1, n):
            cur_sum += nums[i]
            if cur_sum <= nums[i]:
                cur_sum = nums[i]
            
            if cur_sum > max_sum:
                max_sum = cur_sum

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

# leetcode 53 暴力解法, stupid
class Solution2:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return 
        m = max(nums)
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                t = sum(nums[i:j+1])
                if t > m:
                    m = t
        return m

# leetcode 53 动态规划
class Solution3:
    def maxSubArray(self, nums) -> int:
        """f(i) 表示第i个数字结尾的子数组的最大和"""
        if not nums:
            return 
        n = len(nums)
        m = nums[0]
        dp = [None]*n
        dp[0] = m
        for i in range(1, n):
            if dp[i-1]>0:
                dp[i] = nums[i] + dp[i-1]
            else:
                dp[i] = nums[i]
            if dp[i] > m:
                m = dp[i]
        return m
            



if __name__=='__main__':
    array = [84,38,65,52,-9,70,81,58,-33,87,-47,48,23,-53,86,-2,45,56,35,5,90,47,-84,-21,55,-8,37,0,-3,-60,-11,-42,54,-68,-89,-54,-98,68,80,-31,55,-67,93,-45,-21,79,52,-75,12,-12,29,-21,-88,21,57,67,-87,-6,-33,-14,10,32,44,-35,63,54,-13,65,22,-33,-66,-46,0,-73,8,78,82,-62,79,-6,2,-15,72,13,83,30,-20,72,-99,46,-41,11,-21,-97,52,-81,33,-61,83,-45,-18,-83,-15,81,-80,69,37,-98,-93,-7,-28,8,55,-55,-78,38,51,-22,-13,51,-75,45,-61,-20,24,90,-2,-43,-94,-41,-12,-12,-25,72,-54,-28,42,59,-27,25,-70,22,-89,84,66,-91,-1,-6,-14,85,-78,-13,8,-39,66,-68,-72,-58,-11,-89,0,53,-25,51,26,20,-77,-55,-43,-27,46,-14,94,33,-53,37,41,45,-69,-72,7,-48,14,-85,-11,-42,-76,-6,-1,-11,4,98,-58,78,49,44,-25,49,65,31,-78,12,93,-84,-55,-83,52,86,61,59,90,-54,-89,-19,-63,-23,38,-40,47,-86,48,-49,-88,67,-94,38,11,-43,-36,-23,65,-15,65,58,-23,-90,75,-94,72,13,64,62,35,51,-79,72,-72,58,-91,74,72,34,-98,60,1,83,-25,-88,-59,38,-35,-94,99,-70,40,-47,-83,15,-42,88,-94,-78,28,40,73,48,-11,77,-17,-2,29,-68,-68,7,69,9,-9,-56,20,8,59,62,13,35,91,-47,88,84,45,-54,73,27,-55,-22,-56,94,-97,33,71,-15,-92,-23,17,-84,61,-37,24,-48,6,-79,36,-58,82,-51,54,51,-22,42,35,99,64,-15,26,-91,62,47,-97,64,-43,51,-73,-36,-95,20,-21,65,82,-97,93,-35,99,29,-16,82,54,-62,10,-90,79,-78,-91,20,7,12,29,-54,-41,8,87,-8,-41,-86,55,-36,10,-89,-94,-8,89,99,33,88,5,-83,47,-40,-46,-66,-54,-90,-44,-46,30,62,65,-64,84,-99,43,71,-8,-97,61,-76,-57,-29,-89,-75,39,99,-76,-27,65,6,-11,-11,42,20,23,87,6,78,-82,-64,17,60,-29,1,60,91,-27,-70,93,-66,-70,-87,-18,-59,-63,-79,-83,-62,-7,58,20,59,-52,-38,-44,70,-74,61,48,-57,74,-58,-97,-78,42,40,-87,91,46,82,-97,75,94,-16,92,-91,4,86,-77,97,44,42,33,68,80,88,38,-94,49,-37,-75,23,4,-72,22,-76,67,34,91,-10,17,93,-58,-12,-23,-65,-27,58,97,-5,32,18,-86,-35,-13,93,-70,-75,75,55,-35,-99,-21,45,-95,77,68,48,11,37,-62,-72,30,-21,-7,84,-10,65,19,-13,-62,-49,82,-49,-8,-31,-78,21,-30,96,-24,34,73,31,-20,77,8,-75,25,-80,61,62,-76,-31,-81,-7,-70,8,-41,48,72,-27,98,54,23,-10,-77,21,87,-8,18,-37,-96,-32,71,-17,-77,-21,-16,47,-25,-77,-13,-24,-9,-18,68,20,89,-96,-32,61,-24,-57,-8,76,32,14,-3,-4,83,91,58,86,-40,6,-54,-18,85,29,-94,-63,28,-31,12,-81,50,-42,15,40,-62,82,-22,14,-98,70,-10,10,-39,63,-94,-56,55,41,-93,-85,-53,-71,-27,-91,35,-22,-54,-37,47,34,-18,-3,68,96,-86,-93,56,-31,-3,34,-61,86,-55,-24,26,-50,-3,-19,90,3,-5,-85,32,44,-77,-33,-77,-55,29,46,56,87,-80,24,61,-66,7,-6,2,-96,-72,17,66,-28,69,-7,-1,-34,73,-34,69,-54,-20,-22,89,3,21,88,24,-73,34,-20,-85,54,-95,52,64,11,-77,-57,-8,-50,36,-42,-1,5,50,97,71,1,-37,17,46,20,71,12,99,-8,1,23,18,-88,-96,9,42,84,-62,-17,-28,-40,25,63,10,-62,-78,85,43,48,59,-9,-51,98,-92,71,18,78,-16,17,-53,61,-59,64,72,-56,-49,-8,-95,-12,74,-24,25,-23,-83,-88,14,-85,96,-66,62,55,24,88,53,8,59,-28,-14,-80,65,32,80,-94,-26,30,-74,1,98,-93,88,72,-17,13,-51,-24,1,40,-10,-3,73,-48,-71,-25,-83,59,82,76,-92,-31,72,72,77,53,55,-72,-40,80,28,-42,87,-6,-93,-53,83,-67,22,-15,72,-88,58,22,-60,87,96,-43,46,79,-90,53,-75,81,25,78,11,-20,-93,70,-62,11,-95,-98,-95,-88,-52,88,-79,46,-50,92,34,-92,-9,73,94,-12,-93,17,-56,-84,-30,-55,97,72,-77,-15,-48,-94,-44,-34,-6,-63,-33,-2,-75,-9,-37,-55,-63,-11,-86,70,-3,-18,21,-32,46,27,85,66,20,-45,-89,-6,-96,-90,78,-44,92,-89,-2,-14,-52,65,60,-51,-67,-99,-29,-30,-11,-39,-83,62,42,37,-69,-12,-58,-84,-46,61,-53,-59,-45,-49,-49,-67,-17,-80,-56,80,5,-32,22,-58,-7,55,-58,63,-98,31,-75,-82,-30,66,32,0,-68,50,-8,-38,-12,39,3,19,66,30,28,-51,49,48,-94,-69,-84,5,-51,9,-40,-9,-51,-39]
    # array = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    # array = [1, -2, 3, 10, -4, 7, 2, -5]
    s = Solution3()
    print(s.maxSubArray(array))

