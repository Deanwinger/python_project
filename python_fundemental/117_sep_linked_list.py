# leetcode 725. 分隔链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 这题其实很常规, 关键是处理Corner case, 有点烦人, 适合训练
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        head = root
        n = 0
        while root:
            n += 1
            root = root.next
            
        l = n % k
        
        rec = []
        for _ in range(k):
            t = n//k  # k代表有多少组, t代表每组的个数
            rec.append(head)
            if head is None:
                continue

            if t:       
                while t:
                    pre = head                
                    head = head.next
                    t -= 1

            if l:
                pre = head                
                head = head.next
                l -= 1
            
            pre.next = None

        return rec