'''
给定单向链表的头指针和一个结点指针,定义一个函数在O(1)时间删除该结点
'''
#题13

#leetcode 237 简化版

class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None
    def __del__(self):
        self.val = None
        self.next = None

class Solution(object):
    def DeleteNode(self, head, node):
        dummy = node.next
        if not head or not node:
            return 

        #判断是否是尾结点
        if node.next is None:
            if head == node:
                #有可能只有一个node
                node.__del__()
                return
            else:
                #多个node
                while head.next != node:
                    head = head.next
                head.next = None
                node.__del__()
                return 

        #不是尾节点
        node.val = node.next.val
        node.next = node.next.next
        dummy.__del__()
        return


if __name__=='__main__':
    #测试集1
    # node1 = ListNode(10)
    # node2 = ListNode(11)
    # node3 = ListNode(13)
    # node4 = ListNode(15)
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4

    # S = Solution()
    # S.DeleteNode(node1, node3)
    # print(node3.val)
    # print(node2.val)
    # print(node1.val)

    #测试集1
    node1 = ListNode(10)
    S = Solution()
    S.DeleteNode(node1, node1)
    print(node1.val, node1.next)



