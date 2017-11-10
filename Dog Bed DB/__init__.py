# tool.py 是数据库的命令行工具，我们可以通过命令行（即终端）对数据库进行操作。
# interface.py 定义了DBDB类，它对底层的二叉树结构进行封装，开放词典接口以供键值操作。
# logical.py 定义了逻辑层，它是键值操作的抽象接口。
#       LogicalBase 类提供了逻辑更新（比如 get，set 以及 commit）的抽象接口，它同时负责管理存储对象的锁以及对内部节点的解引用。
#       ValueRef 是指向数据库中二进制数据对象的Python对象，是对数据库中数据的引用。
# binary_tree.py 定义了逻辑接口下具体的的二叉树算法。
#       BinaryTree 实现二叉树及其基本操作。值得注意的是，我们实现的是一个数据不可变的二叉树，每次数据更新都会返回一棵新树，新树的大部分数据由于同旧树一致所以直接与旧树共享那部分数据。
#       BinaryNode 实现二叉树中的节点。
#       BinaryNodeRef 是 ValueRef 的子类，实现对二叉树节点的引用。
# physical.py 定义物理层。
#   Storage 类提供持久化的记录存储（也就是写到硬盘上）。

import os

from dbdb.interface import DBDB


__all__= ['DBDB', 'connect']

def connect(dbname):
    try:
        f = open(dbname, 'r+b')
    except IOError:
        fd = os.open(db.name, os.O_RDWR | os.O_CREAT)
        f = os.fdopen(fd, 'r+b')
    return DBDB(f)
