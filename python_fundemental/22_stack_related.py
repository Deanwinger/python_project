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

class StackSquence(object):
    """
    思路： array1先压栈，碰到与array2第一个数字相同的时候开始pop， 
    当stack顶上元素与array2首元素相同时，持续pop， 否则继续压入元素， 
    知道stack顶上元素与array2的首元素相同
    """
    def stack_sequence(self, array1, array2):
        if not array1 and not array2:
            return True
        
        stack = []
        for elem in array1:
            stack.append(elem)
            while len(stack) != 0 and stack[-1] == array2[0]:
                stack.pop()
                array2.pop(0)
        if len(stack) == len(array2) == 0:
            return True
        return False
            

# 8.19 重写        
def stack_sequence(s, t):
    if len(s) != len(t):
        return False

    if not s or not t:
        return False

    stack = []
    for e in s:
        stack.append(e)        
        while stack[-1] == t[0]:
            stack.pop()
            t.pop(0)
            
            if not stack:
                break

    if not stack and not t:
        return True
    return False


    
    

if __name__ == '__main__':
    a = [1]
    b = [2]
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 5, 3, 2, 1]
    # popVF = [4, 5, 2, 1, 3]
    # ops = [1,2,3,4,5]
    # S = Solution()
    # S = StackSquence()
    print(stack_sequence(pushV, popV))
    # print(S.stack_order(pushV, popVF))
    # print(S.stack_order(pushV, ops))
    # print(S.stack_order(a, b))

    # print(S.stack_sequence(pushV, popV))
    # print(S.stack_sequence(pushV, popVF))
    # print(S.stack_sequence(pushV, ops))
    # print(S.stack_sequence(a, b))
