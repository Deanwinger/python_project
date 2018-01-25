'''
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
'''
# 题21
#LeetCode 155. Min Stack


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mylist = []
        self.mysublist = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.mylist:
            self.mylist.append(x)
            self.mysublist.append(x)
        else:
            if x <= self.mysublist[-1]:
                self.mylist.append(x)
                self.mysublist.append(x)
            else:
                self.mylist.append(x)
                self.mysublist.append(self.mysublist[-1])

    def pop(self):
        """
        :rtype: void
        """
        a = self.mylist.pop()
        self.mysublist.pop()
        return a
            
    def top(self):
        """
        :rtype: int
        """
        return self.mylist[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.mysublist[-1]
