'''
输入一个链表，输出该链表中倒数第k个结点。
'''

'''
这道题的思路很好
如果在只希望一次遍历的情况下, 寻找倒数第k个结点, 可以设置两个指针
第一个指针先往前走k-1步, 然后从第k步开始第二个指针指向头结点
然后两个指针一起遍历
当地一个指针指向尾节点的时候, 第二个指针正好指向倒数第k个结点
推广: 寻找中间节点, 两个指针一起, 第一个指针每次走两步, 第二个指针每次走一步,  快指针指到尾部, 慢指针正好指到中间
'''

#leetcode 19. Remove Nth Node From End of List
#题15

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def findKthNode(self, head, k):
        if k <= 0:
            return
        slow = head
        while k > 1 :
            head = head.next
            k -= 1
            #走了k-1步， 最多允许走到链尾（k==1, 代表已经走了k-1步）
            if head.next is None and k != 1:
                raise Exception("超过最大倒数")
        while head.next is not None:
            head = head.next
            slow = slow.next
        return slow


if __name__=='__main__':
    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(13)
    node1.next = node2
    node2.next = node3

    S = Solution()
    # print(S.findKthNode(node1, 1).val)
    print(S.findKthNode(node1, 1).val)