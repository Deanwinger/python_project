'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''
# leetcode 105
#关键在于递归遍历， 关键点就在于找到根节点， 然后对于每个子树，都用找根节点确定左右子树的方式递归的进行下去

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# bug版
# def btree_rebuild(pre_list, mid_list):
#     if (not pre_list) or (not mid_list):
#         return None

#     root = Node(pre_list[0])
#     if len(pre_list) == 1:
#         return 
#     for i in range(len(mid_list)):
#         if root == mid_list[0]:
#             #只有右子树
#             root.right = Node(pre_list[i+1])
#             btree_rebuild(pre_list[1:], mid_list[1:])
#         elif root == mid_list[len(pre_list)-1]:
#             #只有左子树
#             root.left = Node(pre_list[1])
#             btree_rebuild(pre_list[1:], mid_list[:len(pre_list)-1])
#         else:
#             #左右都有
#             root.left = Node(pre_list[1])
#             root.right = Node(pre_list[i+1])

#             l_pre_list = pre_list[1:i+1]
#             l_mid_list = mid_list[:i]
#             left_tree = btree_rebuild(pre_list, mid_list)

#             r_pre_list = pre_list[i+1:]
#             r_mid_list = mid_list[i+1:]
#             right_tree = btree_rebuild(pre_list, mid_list)
    
#     return pre_list[0]

def reConstructBinaryTree(pre, tin):
    if not pre and not tin:
        return None

    if set(pre) != set(tin):
        return None

    root = Node(pre[0])
    i = tin.index(pre[0])
    root.left = reConstructBinaryTree(pre[1:i+1], tin[:i])
    root.right = reConstructBinaryTree(pre[i+1:], tin[i+1:])
    return root
        

    
if __name__ == '__main__':
    pre = [1, 2, 3, 5, 6, 4]
    tin = [5, 3, 6, 2, 4, 1]
    print(reConstructBinaryTree(pre, tin))

