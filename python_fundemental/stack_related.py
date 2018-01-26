'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''

# 题22

class Solution(object):
    def stack_order(self,array1, array2):
        #同时为空
        if not array1 and not array2:
            return True

        stack = []
        for i in array1:
            stack.append(i)
            while len(stack) and stack[-1] == array2[0]:
                stack.pop()
                array2.pop(0)

        if len(stack) == len(array2) == 0:
            return True
        else:
            return False




        


if __name__ == '__main__':
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 5, 3, 2, 1]
    popVF = [4, 5, 2, 1, 3]
    ops = [1,2,3,4,5]
    S = Solution()
    print(S.stack_order(pushV, popV))
    print(S.stack_order(pushV, popVF))
    print(S.stack_order(pushV, ops))

