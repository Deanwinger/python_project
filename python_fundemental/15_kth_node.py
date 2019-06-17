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

#leetcode 19. Remove Nth Node From End of List 此题算是13题和15题的综合版
#题15

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 输入一个链表，输出该链表中倒数第k个结点。
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

    # Remove Nth Node From End of List
    def removeNthFromEnd(self, head, n):
        """
        Corner Case：
        1. 只有一个输入时
        2. 如果删除的节点是head节点
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return
        
        dummy = fast = head
        while fast:
            # 此处用于防止传入的n参数大于链表长度
            if fast.next is None and n != 1:
                raise Exception("错误的参数")
                
            if n == 1:
                break
                
            fast = fast.next
            n -= 1  
             
        while fast.next:      
            temp = head
            fast = fast.next
            head = head.next
            if fast.next is None:
                temp.next = head.next
        return dummy if dummy is not head else dummy.next
        
# 8.5号重做, 感觉这版更易懂, 删除用的是将下一个节点的信息直接拷过来, 特殊情况, 就只有空和一个节点的时候
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return []
        
        dummy = fast = ahead = head
        while n>1:
            fast = fast.next
            n -= 1
        # fast 走到最后一个节点
        while fast.next is not None:
            ahead = head
            fast = fast.next
            head = head.next
            
        # 判断是否是尾节点
        if head.next: 
            head.val = head.next.val
            head.next = head.next.next
        else:
            ahead.next = None
        return dummy

# 2019.6.7重做, 可以尝试用递归的方法坐下, to be finished
# int num;//定义num值
# ListNode* findKthTail(ListNode* pHead, int k) {
#         num = k;
#         if(pHead == NULL)
#             return NULL;
#         //递归调用
#         ListNode* pCur = findKthTail(pHead->next, k);
#         if(pCur != NULL)
#             return pCur;
#         else{
#             num--;// 递归返回一次，num值减1
#             if(num == 0)
#                 return pHead;//返回倒数第K个节点
#             return NULL;
#         }
# }


# 2019-6-17, 引入dum节点, 实现更简单, again, 对于涉及到头结点的变动的, 引入dum节点, 效果不错
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dum = ListNode(0)
        dum.next = head
        
        if n == 1:
            pre = dum
            while head.next:
                pre = head
                head = head.next
            pre.next = None
            return dum.next
        else:
            fast = head
            while n:
                fast = fast.next
                n -= 1

            while fast:
                fast = fast.next
                head = head.next
            head.val = head.next.val
            head.next = head.next.next
            return dum.next

if __name__=='__main__':
    pass