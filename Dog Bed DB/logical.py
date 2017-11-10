# logical.py 定义了逻辑层，它是键值操作的抽象接口。
#       LogicalBase 类提供了逻辑更新（比如 get，set 以及 commit）的抽象接口，它同时负责管理存储对象的锁以及对内部节点的解引用。
#       ValueRef 是指向数据库中二进制数据对象的Python对象，是对数据库中数据的引用。



class LogicalBase(object):
    def get(self, key):
        if not self._storage.locked:
            self._refresh_tree_ref()
        return self._get(self._follow(self._tree_ref), key)

    def _refresh_tree_ref(self):
        self._tree_ref = self.node_ref_class(
            address=self._storage.get_root_address())

    def set(self, key, value):
        if self._storage.lock():
            self._refresh_tree_ref()
        self._tree_ref = self.insert(self._follow(self._tree_ref),
                                    key, self.value_ref_class(value))

    def commit(self):
        self._tree_ref.store(self._storage)
        self._storage.commit_root_address(
            self._tree_ref.address)


class ValueRef(object):
    def store(self, storage):
        if self._referent is not None and not self._address:
            self.prepare_to_store(storage)
            self._address = storage.write(
                self.referent_to_string(self._referent))
