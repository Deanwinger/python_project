

# leetcode 151. Reverse Words in a String
# 题42


class Solu(object):
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

    def reverseWords_v1(self, s):
        """
        解法2: 及其简单的解
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        s = s.split()
        s = s[::-1]
        return " ".join(s)
            


# 拓展 左旋转字符串 类似题 leetcode796. 旋转字符串
class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        if A == "" and B == "":
            return True
        
        n = len(A)
        for i in range(n):
            if A[i] == B[0]:
                print(A[i])
                t = A[i:]+A[:i]
                if t == B:
                    return True
        return False


if __name__ == "__main__":
    test = "the sky is blue"
    s = Solu()
    # print(s.FindNumbersWithSum(test, 15))
    print(s.reverseWords_v1(test))

