"""
    基于dict和循环双链表实现
    1. 如果只用循环双链表, 则无法再O(1)时间get所有键
    2. 因为限制内存空间, 如果只用dict, 需要额外的参数记录dict的大小, 以及数据的加入的先后顺序

    控制循环双链表的长度的逻辑设在哪里呢? 目前暂时采取的是Cache控制, 想过在链表中设定,但是感觉很丑
"""

# leetcode 146. LRU Cache

# 题51

class LRUCache:

    def __init__(self, capacity):
        """
        _map:
        :types capacity: int
        """
        self._map = {}
        self._cdllist = CDLList()
        self._cap = capacity

    def get(self, key):
        """
        :types key: int
        :rtypes: int
        """
        node = self._map.get(key, None)
        if node:
            self._cdllist.set_head(node)
            return node.val
        return -1

    def put(self, key, value):
        """
        :types key: int
        :types value: int
        :rtypes: void
        """
        if self._cap < 1:
            return

        # 查看是否存在, 存在的话, 就地修改
        flag = False
        node = self._map.get(key, None)
        if node:
            # 就地, 非新增
            flag = True
            node.val = value
        else:
            node = DLListNode(key, value)
        self._map[key] = node

        # 创建循环双链表
        # if self._cdllist.is_empty():
        #     self._cdllist.prepend(node)

        # 如果超过限度
        if len(self._map) > self._cap:
            # 删除尾节点, 同时清除dict
            rm_node = self._cdllist.pop_last()
            self._map.pop(rm_node.key)
            # try:
            #     self._map.pop(rm_node.key)
            # except KeyError:
            #     pass

        if flag:
            self._cdllist.set_head(node)
        else:
            self._cdllist.append(node)
            self._cdllist.backwards()

class DLListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next
        

# 循环双链表类
class CDLList:
    
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None
    
    # # 表头插入数据
    # def prepend(self, node):
    #     self._head = node
    #     self._head.next = self._head
    #     self._head.prev = self._head 

    # 弹出表头数据
    def pop(self):
        pass

    # 弹出表尾数据
    def pop_last(self):
        last = self._head.prev
        if self._head.prev is self._head:
            self._head = None
            return last
        last.prev.next = self._head
        self._head.prev = last.prev
        return last

    # 表尾增加数据
    def append(self, node):
        if self.is_empty():
            self._head = node
            self._head.next = self._head
            self._head.prev = self._head 

        last = self._head.prev
        # 原先两个链接断开的顺序有讲究, 下述是OK的
        last.next = node
        node.prev = last
        node.next = self._head
        self._head.prev = node
        return 
    
    # 头节点的指定方法应该是将这个节点移到self._head 这个指针下面,
    def set_head(self, node):
        # 本身就是头节点, 就不用动
        if self._head is node:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        self.append(node)
        self._head = self._head.prev

    def backwards(self):
        self._head = self._head.prev

    def get_inner_value(self):
        n = 6
        print("head is:")
        while n:
            print((self._head.key, self._head.val))
            self._head = self._head.next
            n -= 1
        print("="*40)

if __name__ == "__main__":
# ["LRUCache","put","put","get","get","put","get","get","get"]
# [[2],[2,1],[3,2],[3],[2],[4,3],[2],[3],[4]]
    cache = LRUCache(2)
    cache.put(2,1)
    # cache._cdllist.get_inner_value()
    cache.put(3,2)
    # cache._cdllist.get_inner_value()
    cache.get(3)
    cache._cdllist.get_inner_value()    
    # cache.get(2)
    # cache._cdllist.get_inner_value()
    # cache.put(4,3)
    # print(cache._cdllist._head.val)
    # cache._cdllist.get_inner_value()
    # cache.get(2)
    # cache._cdllist.get_inner_value()