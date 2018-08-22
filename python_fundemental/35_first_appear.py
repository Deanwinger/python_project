'''
在一个字符串(1<=字符串长度<=10000，全部由大写字母组成)中找到第一个只出现一次的字符。
'''

# 题 35 

# leetcode 387. First Unique Character in a String

# 此题很简单， 两次扫描， 第一次放入放入数组， 第二次遍历数组, 查看统计次数是1的index
class Solution(object):
    def firstAppear(self, array):
        alphabet = {}
        for i in array:
            if not alphabet.get(i, None):
                alphabet[i] = 1
            else:
                alphabet[i] += 1
        for j in array:
            if alphabet[j] == 1:
                return j
        return -1

class Solution(object):
    def firstUniqChar(self, s):
        """
        以ascii为例
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        length = len(s)
        rec = [0]*256
        for i in s:
            rec[ord(i)] += 1
        
        for j in range(length):
            indx = ord(s[j])
            if rec[indx] == 1:
                return j
        return -1


# 拓展 leetcode 136. Single Number
# Given a non-empty array of integers, 
# every element appears twice except for one. Find that single one.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res


if __name__=='__main__':
    S = Solution()
    print(S.first_appear('abbaccdeeff'))
    s.print_ascii()
