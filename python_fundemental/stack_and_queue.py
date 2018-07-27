'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
# leetcode 232
#关键在于在stack2, pop操作时, 当stack2为空时, 需将stac1所有的数据一次性放入stack2

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