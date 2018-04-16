from exception import StackUnderflow, QueueUnderflow

#基于list的实现
class Stack(object):
    def __init__(self):
        self.stack = []
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        raise Exception("There is no more stuff")

    def top(self):
        if self.stack:
            return self.stack[-1]
        raise Exception("Empty stack")

    def push(self, val):
        self.stack.append(val)
    
    def is_empty(self):
        return not self.stack
    
    def __repr__(self):
        return "{}".format(type(self).__name__)

class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __del__(self):
        self.val = None
        self.next = None

class Queue(object):
    def __init__(self):
        self.queue = []
    
    def pop(self):
        if self.queue:
            self.queue.pop(0)
        return
    
    def push(self, val):
        self.queue.append(val)
    
    def __repr__(self):
        return "{}".format(type(self).__name__)

#题7  两个栈模拟队列
class queue_by_stack(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        try:
            val = self.stack2.pop()
        except IndexError:
            raise Exception("empty queue")
        else:
            return val
    
    def push(self, val):
        self.stack1.append(val)
    
# 两个队列模拟栈
class stack_by_queue(object):
    pass

#在O(1)时间内求min值的栈
class stack_special_v0(object):
    pass

class SQueue(object):
    def __init__(self, init_len=8):
        self._len = init_len  # length of mem-block
        self._elems = [0]*init_len
        self._head = 0  # index of head element
        self._num = 0   # number of elements
        
    def is_empty(self):
        return self._num == 0
    
    def peek(self):
        if self._num == 0:
            raise QueueUnderflow
        return self._elems[self._head]

    def dequeue(self):
        if self._num == 0:
            raise QueueUnderflow
        e = self._elems[self._head]
        self._head = (self._head+1) % self._len
        self._num -= 1
        return e
    
    def enqueue(self, elem):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head+self._num) % self._len] = elem
        self._num += 1
        
    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0]*self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0



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