'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''

#关键在于递归遍历， 关键点就在于找到根节点， 然后对于每个子树，都用找根节点确定左右子树的方式递归的进行下去

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def btree_rebuild(pre_list, mid_list):
    root = Node(pre_list[0])
    if pre_list == [] and mid_list == []:
        return Node(pre_list[0])
    for i in range(len(mid_list)):
        if pre_list[0] == mid_list[i]:
            root.left = Node(pre_list[1])
            root.right = Node(pre_list[i+1])

            l_pre_list = pre_list[1:i+1]
            l_mid_list = mid_list[:i]
            left_tree = btree_rebuild(pre_list, mid_list)

            r_pre_list = pre_list[i+1:]
            r_mid_list = mid_list[i+1:]
            right_tree = btree_rebuild(pre_list, mid_list)


    
if __name__ == '__main__':
    pre = [1, 2, 3, 5, 6, 4]
    tin = [5, 3, 6, 2, 4, 1]
    print(btree_rebuild(pre, tin))

