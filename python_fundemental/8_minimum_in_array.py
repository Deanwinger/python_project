'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

# 题8

#leetcode 153, 简化了条件, 不存在相等的元素
#特例: [1,0,1,1,1,1], [1,1,1,1,0,1]
#关键在停止条件, start指针和end指针相邻时, 停止
#关键点2, start指针对应的值应该是比end对应的大, 否则,没有旋转
# 2019.2.15

class Solution(object):
    def findMin(self, nums):
        if not nums:
            return 
        # part 1    
        start = 0
        end = len(nums)-1
        if nums[start] < nums[end]:  #关键点2, 表示是顺序
            return nums[0]

        # part 2
        while end-start != 1:
            mid = (start+end) // 2
            if nums[start] == nums[end] == nums[mid]:
                return self.minInOrder(nums)
            if nums[mid] >= nums[start]:
                start = mid
            if nums[end] >= nums[mid]:
                end = midx  
        return nums[end]

    # part 3
    def minInOrder(self, nums):
        min = nums[0]
        for i in nums:
            if i < min:
                min = i
        return min

# 8.9 号, leetcode 153
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 
        
        start = 0
        end = len(nums)-1
        
                    
        if nums[start] < nums[end]:
            return nums[start]
        
        while end >= start:
            mid = (start + end) // 2 
            
            if nums[mid] == nums[start]:
                return nums[end]
            
            if nums[mid] > nums[start]:
                start = mid
                
            if nums[mid] < nums[end]:
                end = mid
        return 

if __name__=='__main__':
    # nums = [1,1,1,1,0,1]
    nums = [1,0,1,1,1,1]
    # nums = [2,3,4,5,1]
    # nums = [1,2]
    # nums = [5,6,7,1,2,3,4]
    s = Solution()
    print(s.findMin(nums))
    