'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''

'''
相当于按层遍历, 中间需要队列做转存
'''

#题23
# leetcode 102, 103, 107类似, 未解决

class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

    def __bool__(self):
        return  False if self.val is None else True

class Solution(object):
    def PrintFromTopToBottom(self, head):
        if not head:
            return
        myqueue = [head,]
        result = []
        while len(myqueue) > 0:
            result.append(myqueue[0].val)
            if myqueue[0].left:
                myqueue.append(myqueue[0].left)
            if myqueue[0].right:
                myqueue.append(myqueue[0].right)
            myqueue.pop(0)
        return result

    def levelOrder(self, root):
        """诀窍在每次将队列的Node弹出来时， 在将左右节点推入队列"""
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return 

    # 8月19号重写, 更简洁
    from queue import Queue
    def PrintFromTopToBottom(self, root):
        # write code here
        que = Queue()
        rec = []
        que.put(root)
        while not que.empty():
            node = que.get()
            if node:
                rec.append(node.val)
                que.put(node.left)
                que.put(node.right)
        return rec



            
if __name__ == '__main__':
    pNode1 = TreeNode(8)
    pNode2 = TreeNode(6)
    pNode3 = TreeNode(10)
    pNode4 = TreeNode(5)
    pNode5 = TreeNode(7)
    pNode6 = TreeNode(9)
    pNode7 = TreeNode(11)

    pNode1.left = pNode2
    pNode1.right = pNode3
    pNode2.left = pNode4
    pNode2.right = pNode5
    pNode3.left = pNode6
    pNode3.right = pNode7

    S = Solution()
    # print(S.PrintFromTopToBottom(pNode1))
    print(S.levelOrder(pNode1))

    #          8
    #     6        10
    #  5    7    9    11