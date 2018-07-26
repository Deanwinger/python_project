'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
对应每个测试案例，输出两个数，小的先输出。
'''

"""
此题的关键要理解,终止条件, 不会出现跳过的情况
|-----|-------|----|--------|-----|
a1    ai      am   an       aj    as
假设恰好存在am+an=t, 小于t时, ai往前移, 大于t时, aj往后移,  
不会出现ai移至an, aj移至am的情况
"""

# 像这种存在“数组”，“查找两个数”关键字的，一律试试头尾各定义两个指针往中间扫描的思路，大多数都会有一些收获。

# 题41

class Solution:
    # 从左右一起查找
    # 因为当两个数的和一定的时候, 两个数字的间隔越大, 乘积越小
    # 所以直接输出查找到的第一对数即可
    def FindNumbersWithSum(self, array, tsum):
        if array == None or len(array) <= 0 or array[-1] + array[-2] < tsum:
            return []
        start = 0
        end = len(array)-1
        while start < end:
            sum = array[start] + array[end]

            if sum < tsum:
                start += 1
            elif sum > tsum:
                end -= 1
            else:
                return [array[start], array[end]]
        return []


# leetcode 829. Consecutive Numbers Sum
# 拓展： 和为S的连续正数序列
class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        pass



if __name__ == "__main__":
    test = [1,2,4,7,11,15]
    s = Solution()
    print(s.FindNumbersWithSum(test, 15))
