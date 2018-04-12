class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Stack(object):
    def __init__(self):
        self.stack = []
    
    def pop(self):
        if self.stack:
            s = self.stack.pop()
            return s
        raise Exception("There is no more stuff")

    def top(self):
        if not self.stack:
            return self.stack[-1]
        raise Exception("Empty stack")

    def push(self, val):
        self.stack.append(val)
    
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

#题7  
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