# leetcode 22. 括号生成
# 《程序员面试金典（第5版）》P230


# 此版本完全照搬230的C++写法, 感觉很不OOP
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left = right = n
        count = 0 # rec 的index
        rec = ['']*2*n
        g = []
        self.add_parentesis(rec, left, right, g, count)
        return g

    def add_parentesis(self, rec, left, right, g, count):
        if left<0 or right < left:
            return 
        # print(rec)
        if left == 0 and right == 0:
            g.append(list(rec))
        else:
            if left > 0:
                rec[count] = ('(')
                self.add_parentesis(rec, left-1, right, g, count+1)
            if right > left:
                rec[count] = (')') 
                self.add_parentesis(rec, left, right-1, g, count+1)
        return 



if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
