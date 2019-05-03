'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
# leetcode 232
#关键在于在stack2, pop操作时, 当stack2为空时, 需将stac1所有的数据一次性放入stack2

# 拓展题 225. 用队列实现栈
# 队列实现栈的关键是， 只能一个队列里保存数据，当需要pop操作时， 先将队列里的数据放入另一个队列留最后一个， 然后将最后一个pop出去
# 具体实现:
    # 实例有两个队列, self.que, self.tem_que, 所有的数据保存在self.que, 
    # 当需要pop的适合, 先将所有的数据(除最后一个外), 导入self.tem_que,
    # pop出来最后一个数据, 然后将self.tem_que的数据导回self.que
# 2019.2.15
# 题7

class queue_by_stack(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, value):
        self.stack1.append(value)
    
    def pop(self):
        if not self.stack2:
            if self.stack1:
                while len(self.stack1) > 0:
                    self.stack2.append(self.stack1.pop())
            else:
                return None
        a = self.stack2.pop()
        return a


# 题7
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mystack1 = []
        self.mystack2 = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.mystack1.append(x)
        # print(self.mystack1)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # print(self.mystack1)
        # print(self.mystack2)
        if self.empty():
            print("I once been here")
            return
        if self.mystack2:
            a = self.mystack2.pop()
            print("a is ", a)
            return a
        else:
            while self.mystack1:
                self.mystack2.append(self.mystack1.pop())
            return self.mystack2.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.mystack2:
            # print("mystack2 is ", self.mystack2)
            return self.mystack2[-1]
        else:
            while self.mystack1:
                self.mystack2.append(self.mystack1.pop())
            return  self.mystack2[-1] if self.mystack2 else None

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.mystack1 and not self.mystack2


# 题225
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que_one = []
        self.que_two = []
        

    def push(self, x: 'int') -> 'None':
        """
        Push element x onto stack.
        """
        if self.empty():
            self.que_one.append(x)
            return
        
        if self.que_one:
            self.que_one.append(x)
        
        if self.que_two:
            self.que_two.append(x)
            
    def pop(self) -> 'int':
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return 
        if self.que_one:
            while len(self.que_one) > 1:
                self.que_two.append(self.que_one.pop(0))
            return self.que_one.pop()
        
        if self.que_two:
            while len(self.que_two) > 1:
                self.que_one.append(self.que_two.pop(0))
            return self.que_two.pop()

    def top(self) -> 'int':
        """
        Get the top element.
        """
        if self.empty():
            return
        
        # top = None
        while self.que_one:
            if len(self.que_one) == 1:
                top = self.que_one[0]
            self.que_two.append(self.que_one.pop(0))

        
        while self.que_two:
            if len(self.que_two) == 1:
                top = self.que_two[0]
            self.que_one.append(self.que_two.pop(0))
        return top        

    def empty(self) -> 'bool':
        """
        Returns whether the stack is empty.
        """
        # print(self.que_one)
        # print(self.que_two)
        if not self.que_one and not self.que_two:
            return True
        return False


# 2019-5-3
# 此版更合理
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que = []
        self.tem_que = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.que.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            raise ValueError("empty stack")
        while len(self.que) != 1:
            self.tem_que.append(self.que.pop(0))
        ret = self.que.pop()
        while len(self.tem_que) > 0:
            self.que.append(self.tem_que.pop(0))
        return ret
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            raise ValueError("empty stack")
        while len(self.que) != 1:
            self.tem_que.append(self.que.pop(0))
        ret = self.que.pop()
        self.tem_que.append(ret)
        while len(self.tem_que) > 0:
            self.que.append(self.tem_que.pop(0))
        return ret
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.que == []

if __name__ == '__main__':
    P = queue_by_stack()
    P.push(10)
    P.push(11)
    P.push(12)
    print(P.pop())
    P.push(13)
    print(P.pop())
    print(P.pop())
    print(P.pop())
    print(P.pop())