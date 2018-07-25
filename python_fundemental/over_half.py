'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''

# 题 29 基于快排的partition, to be finished

# leetcode 169. Majority Element

class Solution:
    def majorityElement(self, nums):
        """
        解法1：基于partition函数的O(n)算法
        :type nums: List[int]
        :rtype: int
        """
        pass


    def majority(self, nums):
        """
        解法2：用字典统计，O(n)
        """
        half = len(nums)//2 + 1
        rec = {}
        for num in nums:
            if not rec.get(str(num), None):
                rec[str(num)] = 1
            else:
                rec[str(num)] += 1
                
            if rec[str(num)] >= half:
                return num
        raise Exception("不存在")

    def majority_elem(self, nums):
        """
        解法3, 比解法2快多了
        :type nums: List[int]
        :rtype: int
        """
        times = 1
        result = nums[0]
        
        for i in range(1, len(nums)):
            if times == 0:
                result = nums[i]
            
            if nums[i] == result:
                times += 1
            else:
                times -= 1
        return result
    