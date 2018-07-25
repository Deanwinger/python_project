'''
在一个字符串(1<=字符串长度<=10000，全部由大写字母组成)中找到第一个只出现一次的字符。
'''

#题 35 此题解答有点问题pass
# 类似题 136. Single Number

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

class Solution:
    def first_appear(self, alist):
        """
        方法2： 创建一个以ascii值为index固定大小的数组， ord()获取ascii值, chr()
        """
        rec = [0]*256

        for s in alist:
            rec[ord(s)] += 1
        r = rec.index(1)
        print(r)
        return chr(r)
        
    def print_ascii(self):
        for num in range(256):
            print(f"{num} is {chr(num)}")



if __name__=='__main__':
    S = Solution()
    print(S.first_appear('abbaccdeeff'))
    s.print_ascii()
