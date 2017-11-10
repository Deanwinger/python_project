# interface.py 定义了DBDB类，它对底层的二叉树结构进行封装，开放词典接口以供键值操作。

from dbdb.physical import Storage
from dbdb.binary_tree import BinaryTree


class DBDB(object):
    def __init__(self, f):
        self._storage = Storage(f)
        self._tree = BinaryTree(self._storage)

    def __getitem__(self, key):
        self._assert_not_close()
        return self._tree.get(key)

    def __setitem__(self, key, value):
        self._assert_not_close()
        return self._tree.set(key, value)

    def _assert_not_close(self):
        if self._storage.closed:
            raise ValueError('database closed...')
