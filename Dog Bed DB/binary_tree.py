# binary_tree.py 定义了逻辑接口下具体的的二叉树算法。
#       BinaryTree 实现二叉树及其基本操作。值得注意的是，我们实现的是一个数据不可变的二叉树，每次数据更新都会返回一棵新树，新树的大部分数据由于同旧树一致所以直接与旧树共享那部分数据。
#       BinaryNode 实现二叉树中的节点。
#       BinaryNodeRef 是 ValueRef 的子类，实现对二叉树节点的引用。


import pickle

from dbdb.logical import LogicalBase, ValueRef


class BinaryTree(LogicalBase):
    def _get(self, node , key):
        while node is not None:
            if key < node.key:
                node = self._follow(node.left_ref)
            elif key > node.key:
                node = self._follow(node.right_ref)
            else:
                return self._follow(node.value_ref)
        raise KeyError

    def _insert(self, node , key, value_ref):
        if node is None:
            new_node = BinaryNode(self.node_ref_class(),
                            key, value_ref, self.node_ref_class(), 1)
        elif key < node.key:
            new_node = BinaryNode.from_node(
                node,
                left_ref=self._insert(
                    self._follow(node.left_ref), key, value_ref))
        elif key > node.key:
            new_node = BinaryNode.from_node(
                node,
                right_ref=self._insert(
                    self._follow(node.right_ref), key, value_ref))
        else:
            new_node = BinaryNode.from_node(node, value_ref=value_ref)
        return self.node_ref_class(reference=new_node)


class BinaryNode(object):
    def store_refs(self, storage):
        self.value_ref.store(storage)
        self.left_ref.store(storage)
        self.right_ref.store(storage)

class BinaryNodeRef(ValueRef):
    @staticmethod
    def referent_to_string(referent):
        return pickle.dumps({
            'left': referent.left_ref.address,
            'right': referent.right_ref.address,
            'key': referent.key,
            'value': referent.value_ref.address,
            'length': referent.length,
            })
