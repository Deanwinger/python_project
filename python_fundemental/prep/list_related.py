# 数据结构与算法分析 第三章 线性表
from exce

# 定义单链表节点
class LNode:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

# 双链表节点
class DLNode(LNode):
    def __init__(self, elem, prev=None, next=None):
        super().__init__(elem, next)
        self.prev = prev

# 3.3 链接表

# 1. 单链表
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
        
# 实用版
# 2. 带尾结点引用的单链表类, 初始化，涉及到表头， 表尾的都需要修改
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

# 3. 循环单链表类
class CLList:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None
    
    def prepend(self, elem):
        p = LNode(elem)
        # 只有一个时， next指针指向自己
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
            self._rear.next = p.next
        return p.elem

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next

# 4. 双链表类, 首尾指针
class DLList(LList1):
    def __init__(self):
        super().__init__()
    
    def prepend(self, elem):
        p = DLNode(elem, prev=None, next=self._head)
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p
        self._head = p

    def append(self, elem):
        p = DLNode(elem, prev=self._rear, next=None)
        if self._head is None:
            self._head = p
        else:
            self._rear.next = p
        self._rear = p

    # 弹出首个节点
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("empty DLList")
        e = self._head.elem
        self._head = self._head.next
        if self._head is None:
            self._rear = self._head
        else:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("empty DLList")
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = self._rear
        else:
            self._rear.next = None
        return e

# 5. 循环双链表类
class CDLList(CLList):
    def __init__(self):
        super().__init__()

    def prepend(self, elem):
        if self._rear is None:
            p = DLNode(elem, None, None)
            self._rear = p
        elif self._rear.next is None: # 只有一个节点
            p = DLNode(elem, prev=self._rear, next=self._rear)
            self._rear.prev = p
            self._rear.next = p
        else:
            p = DLNode(elem, prev=self._rear, next=self._rear.next)
            self._rear.next.prev = p
            self._rear.next = p

    # 同CLList
    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next
    
    # pop out head element 错误版， 一个元素的时候prev 和 next都需要指向自己， 
    # def pop(self):
    #     if self._rear is None:
    #         raise LinkedListUnderflow("empty circular_double_link_list")

    #     p = self._rear.next
    #     if self._rear is p:
    #         # 只有一个元素，弹出自身
    #         self._rear = None
    #     if p.next is self._rear:
    #         # 只有两个元素
    #         self._rear.prev = None
    #         self._rear.next = None
    #     else:
    #         p.next.prev = self._rear
    #         self._rear.next = p.next
    #     return p.elem

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow("empty circular_double_link_list")
        p = self._rear.next
        if self._rear is p: #只有一个元素时
            self._rear = None
        else:
            p.next.prev = self._rear
            self._rear.next = p.next
        return p.elem


    # pop out last element 错误版， 一个元素的时候prev 和 next都需要指向自己，
    # def pop_last(self):
    #     if self._rear is None:
    #         raise LinkedListUnderflow("empty circular_double_link_list")
    #     p = self._rear.prev
    #     if self._rear is p: #只有一个元素
    #         self._rear = None
    #     elif p.next is self._rear: 
    #         self._rear = self._rear.prev
    #         self._rear.next = None
    #         self._rear.prev = None
    #     else:
    #         self._rear.pre.next = self._rear.next
    #         self._rear.next.prev = self._rear.prev
    #         self._rear = self._rear.prev

    def pop_last(self):
        if self._rear is None:
            raise LinkedListUnderflow("empty circular_double_link_list")

        e = self._rear.elem
        p = self._rear.prev
        if self._rear is p: # 只有一个元素
            self._rear = None
        else:
            self._rear.next.prev = p
            p.next = self._rear.next
            self._rear = p
        return e

## 所有的接口都待测试