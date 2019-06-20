# 45 题

# leetcode 类似题390. Elimination Game

class LinkNode(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Solution:
    def LastRemaining_Solution(self, n, m):
        """数学解法"""
        if n < 1 or m < 1:
            return -1
        remainIndex = 0
        for i in range(1, n+1):
            remainIndex = (remainIndex + m) % i
        return remainIndex

    def LastRemaining(self, n, m):
        """
        链表解法, 
        0, 1, 2, 3, 4...
        报数分别是1, 2, 3   
        """
        if n < 1 or m < 1:
            return -1
        # 构建链表
        node = head = LinkNode(0)
        for i in range(1, n):
            head.next = LinkNode(i)
            head = head.next
        head.next = node

        # 核心代码
        count = 1
        while node.next != node:
            if count == m:
                node.val = node.next.val
                node.next = node.next.next
                count = 1
                continue
            node = node.next
            count += 1
        return node.val

#8.22重写, 更易懂, 数到m
# 哈哈哈, 错误答案哥哥啊, 你m取1试试, 这个牛客网,真是不靠谱啊, 把这个答案通过了;
def last_remaining(n, m):
    if n < 1 or m < 1:
        return -1

    node = head = LinkNode(0)
    for i in range(1, n):
        head.next = LinkNode(i)
        head = head.next
    head.next = node

    t = m
    while node.next is not node:
        slow = node
        node = node.next
        t -= 1
        if t == 1:
            slow.next = node.next
            node = node.next
            t = m
    return node.val

# 8.22 正确版
def last_remaining_v1(n, m):
    if n < 1 or m < 1:
        return -1

    node = head = LinkNode(0)
    for i in range(1, n):
        head.next = LinkNode(i)
        head = head.next
    head.next = node

    if m == 1:
        return  n-1

    count = 1
    while node.next is not node:
        slow = node
        node = node.next
        count += 1  
        if count == m:
            slow.next = node.next
            node = node.next
            count = 1
    return node.val

class ListNode(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None

# 2019-4-16 continue 是关键, 因为c=1的时候,相当于重新开始了一轮喊取, 所有要continue
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1

        dum = head = ListNode(0)
        for i in range(1, n):
            head.next = ListNode(i)
            head = head.next
        head.next = dum
        head = head.next
        
        c = 1 
        while head.next is not head:
            if c == m:
                head.val = head.next.val
                head.next = head.next.next
                c = 1
                continue
            c += 1
            head = head.next
        return head.val

# 2019-6-20 这个题目每次复习的时候都可以再做一遍
class LinkNode(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1
        
        # 构建链表
        node = head = LinkNode(0)
        for i in range(1, n):
            head.next = LinkNode(i)
            head = head.next
        head.next = node
        
        starter = node
        
        while starter.next is not starter:
            t = m-1
            while t:
                t -= 1
                starter = starter.next
            starter.val = starter.next.val
            starter.next = starter.next.next
        return starter.val


if __name__=="__main__":
    s = Solution4()
    # from random import randint

    # n = 1
    # while n:
    #     a = randint(1, 100)
    #     b = randint(1, a)
    #     print("cur is: ", n)
    #     ans1 = s.LastRemaining(a, b)
    #     ans2 = last_remaining_v1(a, b)
    #     print("="*20, ans1)
    #     print("="*20, ans2)
    #     if n == 50:
    #         break
    #     if ans1 != ans2:
    #         print("cur a is: ", a)
    #         print("cur b is: ", b)
    #         break
    #     n += 1
    a = s.LastRemaining_Solution(5, 3)
    print(a)