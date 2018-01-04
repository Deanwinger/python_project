#单例实现

#1, __new__方法实现
class singletona(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(singletona, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class myclass(singletona):
    a = 1


a = myclass()
b = myclass()

print(id(a))
print(id(b))

print(a == b)            # True
print(a is b)            # True

b.num = 3
print(a.num)             # 3


#2,
#3,
#4,
#拓展1, super和__new__
