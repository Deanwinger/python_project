from array import array
import reprlib
import math


class Vector:
    typecode = 'd'

    def __init__(self, components):
        """array 构造方法的第一个参数指定了数组中数字的存储方式。"""
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    # reprlib.repr用于生成大型结构或递归结构的安全表示形式,它会限制输出字符串的长度,用 '...'表示截断的部分。
    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
