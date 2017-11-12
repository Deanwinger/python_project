# physical.py 定义物理层。
#   Storage 类提供持久化的记录存储（也就是写到硬盘上）。
import os
import struct

import portalocker

class Storage(object):
    # 文件开头的部分划给了超级块，在这里由它保存整个数据库文件的一些基本信息
    SUPERBLOCK_SIZE = 4096
    INTEGER_FORMAT = "!Q"
    INTEGER_LENGTH = 8

    def __init__(self, f):
        self._f = f
        self.locked = False
        self._ensure_superblock()

    def _ensure_superblock(self):
        self.lock()
        #f.seek()函数移动文件指针到指定的位置
        self._seek_end()
        end_address = self._f.tell()
        if end_address < self.SUPERBLOCK_SIZE:
            self._f.write(b'\x00' * (self.SUPERBLOCK_SIZE - end_address))
        self.unlock()

    def lock(self):
        if not self.locked:
            portalocker.lock(self._f, portalocker.LOCK_EX)
            self.locked = True
            return True
        else:
            return False

    def unlock(self):
        if self.locked:
            self._f.flush()
            portalocker.unlock(self._f)
            self.locked = False

    def _seek_end(self):
        self._f.seek(0, os.SEEK_END)

    def _seek_superblock():
        #移动文件指针到文件开始位置
        self._f.seek(0)

    # 每一个数据块的开头会记录这段数据的大小，随后记录数据块的内容。
    # 因此写的时候会先写大小，随后写数据，同样读的时候会先读数据大小，
    # 接着读取相应大小的数据
    def _bytes_to_integer(self, integer_bytes):
        return struct.unpack(self.INTEGER_FORMAT, integer_bytes)[0]

    def _integer_to_bytes(self, integer):
        return struct.pack(self.INTEGER_FORMAT, integer)

    def _read_integer(self):
        return self._bytes_to_integer(self._f.read(self.INTEGER_LENGTH))

    def _write_integer(self):
        self.lock()
        self._f.write(self._integer_to_bytes(integer))

    def write(self, data):
        self.lock()
        self._seek_end()
        object_address = self._f.tell()
        self._write_integer(len(data))
        self._f.write(data)
        return object_address

    def read(self, address):
        self._f.seek(address)
        length = self._read_integer()
        data = self._f.read(length)
        return data

    def commit_root_address(self, root_address):
        self.lock()
        self._f.flush()
        self._seek_superblock()
        self._write_integer(root_address)
        self._f.flush()
        self.unlock()

    def get_root_address(self):
        # 定位到超级块的地址（也就是文件开头）
        self._seek_superblock()
        root_address = self._read_integer()
        return root_address

    def close(self):
        self.unlock()
        self._f.close()

    @property
    def closed(self):
        return self._f.closed
