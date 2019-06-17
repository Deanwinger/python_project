'''
给定单向链表的头指针和一个结点指针,定义一个函数在O(1)时间删除该结点
'''
#题13

#leetcode 237 简化版
# leetcode 203 类似题

class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None
    def __del__(self):
        self.val = None
        self.next = None

# class Solution(object):
#     def DeleteNode(self, head, node):
#         dummy = node.next
#         if not head or not node:
#             return 

#         #判断是否是尾结点
#         if node.next is None:
#             if head == node:
#                 #有可能只有一个node
#                 node.__del__()
#                 return
#             else:
#                 #多个node
#                 while head.next != node:
#                     head = head.next
#                 head.next = None
#                 node.__del__()
#                 return 

#         #不是尾节点
#         node.val = node.next.val
#         node.next = node.next.next
#         dummy.__del__()
#         return

# 8.9号 非常漂亮
class Solution:
    def removeElements(self, head, node):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 如果只有一个或者没有, 直接return None
        if head is None or head.next is None:
            return
        
        dummy = head
        # 判断尾节点
        if node.next is None:
            while head is not node:
                slow = head
                head = head.next
            slow.next = None
            return dummy

        # 非尾节点
        node.val = node.next.val
        node.next = node.next.next
        return dummy

# leetcode 203. 移除链表元素
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 聪明一点的处理是先建立一个临时节点, 明显优雅多了, 之所以要创建一个临时节点, 是因为, 可能涉及到第一个节点的修改, 所有, 这是一个有用的技巧
        pre = dum = ListNode(0)
        dum.next = head
        
        while head:
            if head.val == val:
                tem = head.next
                pre.next = head.next
                head = tem
                continue
            pre = pre.next
            head = head.next
        return dum.next

if __name__=='__main__':
    # 测试集1
    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(13)
    node4 = ListNode(15)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    S = Solution()
    S.removeElements(node1, node3)
    print(node3.val)
    print(node2.val)
    print(node1.val)

    #测试集1
    # node1 = ListNode(10)
    # S = Solution()
    # S.DeleteNode(node1, node1)
    # print(node1.val, node1.next)



