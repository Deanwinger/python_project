'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''
#题14
# leetcode 328. Odd Even Linked List, 使用的是linked_list, 这题有点tricky, 参考下面的注释

class Solution(object):
    def reorder_odd_even(self, array):
        if len(array) <= 1:
            return
        j = len(array) - 1
        for i in range(len(array)):
            if self.is_even(array[i]):
                #偶数， 则开始判断尾部
                while self.is_even(array[j]):
                    j -= 1
                if i >= j:
                    return array
                else:
                    array[i], array[j] = array[j], array[i]
        return

    def is_even(self, n):
        return n % 2 == 0


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        
        dummy1 = even = ListNode(0)
        dummy2 = odd = ListNode(0)
        i = 1
        while head:
            if self.is_odd(i):
                odd.next = head
                odd = odd.next 
            else:
                even.next = head
                even = even.next
                
            head = head.next
            odd.next = None # 此两条件非常重要, 不难忽视
            even.next = None
            i += 1
            
        odd.next = dummy1.next
        return dummy2.next
    
    def is_odd(self, x):
        return x%2 == 1



if __name__=='__main__':
    n = 2        
    dummy = head = ListNode(1)
    while n<20:
        head.next = ListNode(n)
        head = head.next
        n += 1
    s = Solution()
    h = s.oddEvenList(dummy)
    h = dummy
    print("Cur list is: ")
    while h:
        print(h.val, "->", end='  ')
        h = h.next
    print('None')
