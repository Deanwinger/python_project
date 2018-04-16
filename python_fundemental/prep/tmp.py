
class QueueUnderflow(ValueError):
    pass

class StackUnderflow(ValueError):
    pass


class SStack(): 
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return not self._elems

    def top(self):
        if not self._elems:
            raise StackUnderflow
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if not self._elems:
            raise StackUnderflow
        return self._elems.pop()

class BinTNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
if __name__ == "__main__":
    root = BinTNode(1, BinTNode(2, BinTNode(3), BinTNode(4)), BinTNode(5))
    # levelorder(root, print)
