'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''

class ListNode(object):
    def __init__(self, value=None):
        self.val = value
        self.next = None

class Solution(object):
    def merge_link_list(self, head1, head2):
        print(head1.val, '*'*8, head2.val)
        dummy = head = ListNode()
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        #如果不想额外增加空间, 递归
        if head1.val <= head2.val:
            print(head1.val)
            head.next = head1
            head= head.next
            head1 = head1.next
            head.next = self.merge_link_list(head1, head2)
        else:
            print(head2.val)
            head.next = head2
            head= head.next
            head1 = head2.next
            head.next = self.merge_link_list(head1, head2)
        return dummy

            
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
    a = S.merge_link_list(node1, node4)
    while a:
        print(a.val)
        a = a.next
