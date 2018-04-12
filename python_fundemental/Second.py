from Second_data_structure import Stack, Node, TreeNode

#题3
def two_dims_array():
    pass

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

    pre = [1, 2, 3, 5, 6, 4]
    tin = [5, 3, 6, 2, 4, 1]
    print(btree_rebuild(pre, tin))