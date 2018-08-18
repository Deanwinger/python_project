'''
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
'''

# leetcode 155. Min Stack
# 题21


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mylist = []
        self.submylist = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.mylist.append(x)
        if not self.submylist:
            self.submylist.append(x)
        else:
            tem = self.submylist[-1]
            if tem < x:
                self.submylist.append(tem)
            else:
                self.submylist.append(tem)
        return
        

    def pop(self):
        """
        :rtype: void
        """
        if not self.mylist:
            return None
        self.mylist.pop()
        self.submylist.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if not self.mylist:
            return
        return self.mylist[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.mylist:
            return
        return self.submylist[-1]
        

class MinStack_V1(object):
    """使用双stack"""
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min_stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._stack.append(x)
        if not self._min_stack:
            self._min_stack.append(x)
        else:
            if self._min_stack[-1] > x:
                self._min_stack.append(x)
            else:
                self._min_stack.append(self._min_stack[-1])

    def pop(self):
        """
        :rtype: void
        """
        if self._stack:
            self._stack.pop()
            self._min_stack.pop()
        else:
            raise Exception("empty stack")
        

    def top(self):
        """
        :rtype: int
        """
        if self._stack:
            return self._stack[-1]
        else:
            raise Exception("empty stack")
        

    def getMin(self):
        """
        :rtype: int
        """
        if self._min_stack:
            return self._min_stack[-1]
        else:
            raise Exception("empty stack")

# 非常elegant解法
class MinStack_V2(object):
    """使用tuple"""
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin = self.getMin()
        if curMin is None:
            curMin = x
        else:
            if curMin > x:
                curMin = x
        self._stack.append((x, curMin))

    def pop(self):
        """
        :rtype: void
        """
        return self._stack.pop()[0] if self._stack else None
        

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1][0] if self._stack else None

    def getMin(self):
        """
        :rtype: int
        """
        return self._stack[-1][1] if self._stack else None