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
