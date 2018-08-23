

# leetcode 151. Reverse Words in a String
# 题42


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        pass


# 拓展 左旋转字符串 类似题 leetcode796. 旋转字符串
'''
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
'''
class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        pass


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        if not s:
            return
        
        s = ' '.join(s)
        n = len(s)
        
        rec = []
        strs = s[::-1]
        start = end = 0
        while end < n:
            print(strs)
            if strs[end] == ' ' or end == n-1:
                if end == n-1:
                    end = n
                t = self.reverse_word(strs, start, end)
                rec.append(t)
                start = end+1
            end += 1
        return ' '.join(rec)
    
    def reverse_word(self, s, start, end):
        s = s[start:end]
        return s[::-1]

if __name__ == "__main__":
    test = "the sky is blue"
    s = Solution()
    # print(s.FindNumbersWithSum(test, 15))
    print(s.reverseWords(test))

