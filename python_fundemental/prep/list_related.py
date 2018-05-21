# 数据结构与算法分析 第三章 线性表

# 自定义错误
class LinkedListUnderflow(ValueError):
    pass

# 定义节点
class LNode:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

# 3.3 链接表

# 1 单链表
class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None
    
    # 表头插入数据
    def prepend(self, elem):
        self._head = LNode(elem, self._head)
    
    # 弹出表头数据
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("empty LList")
        e = self._head.elem
        self._head = self._head.next
        return e

    # 弹出表尾数据
    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("empty LList")
        p = self._head

        if p.next is None:  # list with only one element
            e = p.elem
            self._head = None
            return e

        while p.next.next:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next:
            p = p.next
        p.next = LNode(elem)

    def printall(self):
        p = self._head
        while p:
            print(p.elem, end='')
            if p.next:
                print(',', end='')
            p = p.next
        print('')
        


# 带尾结点引用的单链表类, 初始化，涉及到表头， 表尾的都需要修改
class LList1(LList):
    def __init__(self):
        super().__init__()
        self._rear = None
    
    # 表头插入数据, 覆盖超类的方法
    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    # 弹出表尾数据
    def pop_last(self):
        if self._head is None: # empty list
            raise LinkedListUnderflow("empty LList")
        p = self._head
        if p.next is None: # list with only one element
            e = p.elem
            self._head = None
            self._rear = None
            return e
        while p.next.next:
            p = p.next
        self._rear = p
        e = p.next.elem
        p.next = None
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
            return
        self._rear.next = LNode(elem)
        self._rear = self._rear.next

# 循环单链表类
class LCList:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None
    
    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p
        return

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next
    
    # pop out head element
    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow("empty link")

        p = self._rear.next     
        if self._rear is p:
            self._rear = None
        else:        
            self._rear = self._rear.next.next
        return p.elem

    def printall(self):
        if self.is_empty():
            return
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next

# 双链表类

# 循环双链表类