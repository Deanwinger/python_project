'''
在一个字符串(1<=字符串长度<=10000，全部由大写字母组成)中找到第一个只出现一次的字符。
'''

#题 35
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


if __name__=='__main__':
    S = Solution()
    print(S.firstAppear('abaccdeff'))
