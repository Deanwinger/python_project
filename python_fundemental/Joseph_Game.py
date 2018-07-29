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
        dummy = head = LinkNode(0)
        for i in range(1, n):
            head.next = LinkNode(i)
            head = head.next
        head.next = dummy

        count = 1
        while dummy.next != dummy:
            if count == m:
                print(dummy.val)
                dummy.val = dummy.next.val
                dummy.next = dummy.next.next
                count = 1
                continue
            count += 1
            dummy = dummy.next
        return dummy.val


if __name__=="__main__":
    s = Solution()
    print("="*20, s.LastRemaining(2, 2))