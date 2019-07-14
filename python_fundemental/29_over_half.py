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
    
# 2019-6-19 当单独使用partition时, 是需要考虑lo, hi的边界条件的, 即lo>=hi:return hi, 其实就是只有两个元素的时候; 这也是为什么函数主体中需要先判断空和一个元素的case
# 貌似又不需要考虑上面的边界, 因为单边选择的时候, 基础case是2个元素, 此处有误, 应该是==更合理;
# 反复体会partition
class Solution2:
    def majorityElement(self, nums) -> int:
        n = len(nums)
        if not n:
            return 
        if n== 1:
            return nums[0]
        
        mid = n//2
        start = 0
        end = n-1
        index = self.partition(nums, start, end)
        while index != mid:
            if index < mid:
                start = index+1 
                index = self.partition(nums, start, end)
            else:
                end = index - 1
                index = self.partition(nums, start, end)
        return nums[index]
            
    def partition(self, nums, lo, hi):
        # 非常关键, corner case [2, 3], 没有该条件就直接报错
        if lo== hi:
            return hi
        i = lo+1
        j = hi

        pivot = lo
        while True:
            while nums[i] < nums[pivot]:
                if i == hi:
                    break
                i += 1

            while nums[j] > nums[pivot]:
                if j == lo:
                    break
                j -= 1

            if i>=j:
                break
            else:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        nums[lo], nums[j] = nums[j], nums[lo]
        return j
            
    
if __name__ == "__main__":
    nums = [2,3]
    s = Solution2()
    print(s.majorityElement(nums))