'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''
#leetcode 题

class ListNode(object):
    def __init__(self, value=None):
        self.val = value
        self.next = None

class Solution(object):
    def merge_link_list(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        #如果不想额外增加空间, 递归
        if head1.val <= head2.val:
            head = head1
            head1 = head1.next
            head.next = self.merge_link_list(head1, head2)
        else:
            head = head2
            head2 = head2.next
            head.next = self.merge_link_list(head1, head2)
        return head

    def mergeLinkList(self, l1, l2):
        #非递归实现
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

            
if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(5)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(2)
    node5 = ListNode(4)
    node6 = ListNode(6)
    node4.next = node5
    node5.next = node6

    S = Solution()
    # a = S.merge_link_list(node1, node4)
    a = S.mergeLinkList(node1, node4)
    while a:
        print(a.val)
        a = a.next
