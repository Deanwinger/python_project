# leetcode 26. 删除排序数组中的重复项


# leetcode 80. 删除排序数组中的重复项 II

# 2019-5-13
# 26 这题还有点tricky, 好好看看
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        cur = 0
        pre = 0
        while cur < n:
            if nums[cur] == nums[pre]:
                cur += 1
            else:
                pre += 1
                nums[pre] = nums[cur]
                cur += 1
        return pre+1


# 2019-5-14
# 80
'''
对于这种题目, 很烦的就是需要保持多个状态, 或者多个指针, 很容易出错, 应该有简洁的解决方法, to be finished

下面的答案值得好好研究, a copy from other's
'''

class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 如果是空则返回0
        if not nums:
            return 0
        index, count = 1, 1
        for i in range(1, len(nums)):
            # 如果两个字符相等
            if nums[i-1] == nums[i]:
                # count计数自增一次
                count += 1
            # 如果不等，count重置为1
            else:
                count = 1
            # 如果count小于等于2，则把nums[i]放到有效位置的后一个位置
            if count <= 2:
                nums[index] = nums[i]
                index += 1
        # 删除无用元素[也可不用删除，LeetCode不会检查后面的元素]
        return index


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    so = Solution()
    res = so.removeDuplicates(nums)
    print(res, nums)
