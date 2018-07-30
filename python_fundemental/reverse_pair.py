'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。
'''

# 题36 
# 类似题 leetcode 629. K个逆序对数组
# leetcode 315. Count of Smaller Numbers After Self
class Solution(object):
    def InversePairs(self, data):
        if not data:
            return 0
        length = len(data)
        copy = [0]*length
        for i in range(length):
            copy[i] = data[i]
        count = self.InversePairsCore(data, copy, 0, length-1)
        return count
    
    def InversePairsCore(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        
        length = (end - start) // 2
        left = self.InversePairsCore(copy, data, start)

        




if __name__=='__main__':
    s = Solution()
    nums = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,
            601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,
            486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,
            882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,
            697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,
            3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
    print(s.InversePairs(nums))
    print(len(nums))