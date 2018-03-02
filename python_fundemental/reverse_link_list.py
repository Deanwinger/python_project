'''
输入一个链表，从尾到头打印链表每个节点的值。
'''

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Solution(object):
    def link_reverse(self, Node):
        if Node.next == None:
            return None
        
        stack = Stack()
        head = Node
        while head:
            stack.push(head)
            head = head.next
        
        while stack.stack:
            print(stack.pop().value)
        return 

class Stack(object):
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if not self.stack:
            return
        else:
            return self.stack.pop()
    
    def top(self):
        if not self.stack:
            return
        else:
            return self.stack[-1]

if __name__ == '__main__':
    node1 = Node(10)
    node2 = Node(11)
    node3 = Node(13)
    node1.next = node2
    node2.next = node3

    singleNode = Node(12)

    test = Node()

    S = Solution()
    print(S.link_reverse(node1))
    print(S.link_reverse(test))
    print(S.link_reverse(singleNode))
