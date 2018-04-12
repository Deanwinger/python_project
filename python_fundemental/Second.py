from Second_data_structure import Stack, Node, TreeNode

#待完成， java数据结构的API

#题3
def two_dims_array(alist, target):
    if not alist:
        return False

    rows = len(alist)
    cols = len(alist[0])

    i = 0
    j = cols-1
    print("i is: %s"%i)
    print("j is: %s"%j)
    while i < rows and j >= 0:
        if target > alist[i][j]:
            i += 1
        elif target < alist[i][j]:
            j -= 1
        else:
            return True
    return False

#题5
def print_linked_list_reversely(node):
    s = Stack()
    while node:
        s.push(node)
        node = node.next

    while True:
        try:
            val = s.pop().val
            if val:
                print(val)
        except Exception:
            break
    print("Done")
    return
    
#题6
def btree_rebuild(pre, tin):
    print("="*10, pre)
    print("="*10, tin)
    if len(pre) != len(tin):
        raise Exception("错误的参数")
    
    if not pre and not tin:
        return 
    
    root = Node(pre[0])
    i = tin.index(pre[0])
    root.left = btree_rebuild(pre[1:i+1], tin[:i])
    root.right = btree_rebuild(pre[i+1:], tin[i+1:])
    return root

# def btree_revisit(root):
#     #先序

#     #中序

#     #后序

#题8 旋转数组的最小数字
def minmum_in_array(alist):
    pass


#题9 fibonacci 0, 1, 1, 2, 3, 5
def fibonacci(n):
    if n <= 0:
        raise Exception("错误的参数")
    if n == 1:
        return 0
    if n == 2:
        return 1
    fibOne = 0
    fibTwo = 1
    i = 2
    while i < n:
        fibN = fibOne + fibTwo
        fibOne =  fibTwo
        fibTwo = fibN
        i += 1
    return fibN




if __name__ == "__main__":
    # l_list_1 = Node()
    # l_list_2 = Node(1)

    # l_list_3 = Node(10)
    # node2 = Node(11)
    # node3 = Node(13)
    # l_list_3.next = node2
    # node2.next = node3

    # print_linked_list_reversely(l_list_1)
    # print_linked_list_reversely(l_list_2)
    # print_linked_list_reversely(l_list_3)

    # pre = [1, 2, 3, 5, 6, 4]
    # tin = [5, 3, 6, 2, 4, 1]
    # print(btree_rebuild(pre, tin))

    print(fibonacci(8))