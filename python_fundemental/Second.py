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


#题5
def print_linked_list_reversely(node):
    s = Stack()
    while node:
        s.push(node)
        node = node.next

    while True:
        try:
            val = s.pop().val
            if val:
                print(val)
        except Exception:
            break
    print("Done")
    return
    
if __name__ == "__main__":
    l_list_1 = Node()
    # l_list_2 = Node(1)

    # l_list_3 = Node(10)
    # node2 = Node(11)
    # node3 = Node(13)
    # l_list_3.next = node2
    # node2.next = node3

    print_linked_list_reversely(l_list_1)
    # print_linked_list_reversely(l_list_2)
    # print_linked_list_reversely(l_list_3)