'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
# leetcode 232
#关键在于在stack2, pop操作时, 当stack2为空时, 需一次性将stac1所有的数据放入stack2

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