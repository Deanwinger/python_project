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
        