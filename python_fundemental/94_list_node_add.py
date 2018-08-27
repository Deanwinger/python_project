# leetcode 445. 两数相加 II

# There is no maximum of INT in python, so.....

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        解法1: Python 没有数字限制
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x1, x2 = 0, 0
        while l1:
            x1 = x1*10+l1.val
            l1 = l1.next
        while l2:
            x2 = x2*10+l2.val
            l2 = l2.next
        x = x1 + x2
        
        head = ListNode(0)
        if x == 0: return head
        while x:
            v, x = x%10, x//10
            head.next, head.next.next = ListNode(v), head.next
            
        return head.next
    
    def addTwoNumbers_v1(self, l1, l2):
        """
        8.27 日再次尝试, 发现还是写成了一坨屎, 未通过, 卒;
        解法2: 逆序, 然后逐个想加, to be finished
        """
        if not l1:
            return l2
        
        if not l2:
            return l1
        # 第一步, 逆序
        head1, m = self.reverse_llist(l1)
        head2, n = self.reverse_llist(l2)

        dummy = head =  ListNode(hea1.val+head2.val)

        flag = False
        steps = min(m, n)
        while steps:
            val = hea1.val + head2.val
            if flag:
                val += 1
                if val >= 10:
                    val -= 10
                    flag = True
                else:
                    flag = False
            head.next = ListNode(val)
            head = head.next
            head1 = head1.next
            head2 = head2.next
            steps -= 1
        
        while head1:
            val = head1.val
            if flag:
                val += 1
                if val >= 10:
                    val -= 10
                    flag = True
                else:
                    flag = False
            head.next = ListNode(val)
            head = head.next
            head1 = head1.next

        while head2:
            val = head2.val
            if flag:
                val += 1
                if val >= 10:
                    val -= 10
                    flag = True
                else:
                    flag = False
            head.next = ListNode(val)
            head = head.next
            head2 = head2.next            
        
        h = self.reverse_llist(self, dummy)
        return h

        


    def reverse_llist(self, root):
        head = root
        root = root.next
        head.next = None
        count = 1
        while root:
            tem = root.next
            root.next = head
            head = root
            root = tem
            count += 1
        return root, count
        


        