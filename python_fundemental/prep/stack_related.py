"""
    栈的实现
    1. 两种实现方式已经finished
    2. 基础应用待完成
"""

from exception import StackUnderflow
from list_related import LNode

# 基于顺序表的实现
class SStack:
    def __init__(self):
        self._elems = []
    
    def is_empty(self):
        return not self._elems

    def top(self):
        if not self._elems:
            raise StackUnderflow("empty SStack")
        return self._elems[-1]
    
    def push(self, elem):
        self._elems.append(elem)

    # 弹出最后一个元素
    def pop(self):
        if not self._elems:
            raise StackUnderflow("empty SStack")
        return self._elems.pop()

# 基于链接表概念（链接结点）实现的栈类
# 表头做栈顶， 表尾做栈底
class LStack:
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow("empty LStack")
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderflow("empty LStack")
        e = self._top.elem
        self._top = self._top.next
        return e

if __name__ == '__main__':
    st = SStack()
    st.push(1)
    st.push(5)
    print(st.pop())
    print(st.top())
    print(st.pop())
    print(st.is_empty())
    st.top()