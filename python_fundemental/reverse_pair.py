'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。
'''

# 题36
# 315. Count of Smaller Numbers After Self
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        start = 0
        end = len(nums)-1
        a = self.recursivelyDivid(nums, start, end)
        return 
    
    def recursivelyDivid(data, start, end):
        # if start == end:
        #     return start
        # mid = (start + end) // 2
        # self.recursivelyDivid(data, start, mid)
        # self.recursivelyDivid(data, mid, end)
        pass


        




if __name__=='__main__':
    nums = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,
            601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,
            486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,
            882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,
            697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,
            3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
    countSmaller()