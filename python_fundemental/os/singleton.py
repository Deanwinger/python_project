# 单例
# I don’t really see the need, as a module with functions (and not a class) would 
# serve well as a singleton. All its variables would be bound to the module, which 
# could not be instantiated repeatedly anyway. If you do wish to use a class, 
# there is no way of creating private classes or private constructors in Python, 
# so you can’t protect against multiple instantiations, other than just via convention 
# in use of your API. I would still just put methods in a module, and consider the module 
# as the singleton.
# 也就是说，实际上，python中，如果我们只用一个实例，直接这么写就行

# some module.py
class SingletonClass:
    pass

# 在别处我们想用这个实例都直接使用 module.single_instance 这个实例就好。
# 这是最简单也是最直观的一种方式,嗯，直接导入这个实例用，而不是导入class，简单粗暴
single_instance = SingletonClass()

# ========================================================================

# 其他实现：

# http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
# http://python.jobbole.com/87294/
# 此处还有讲各种方法的优劣
class BaseClass:
    pass

# 方法一：装饰器实现
def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class MyClass(BaseClass):
    pass
"""
Pros

    Decorators are additive in a way that is often more intuitive than multiple inheritance.

Cons

    While objects created using MyClass() would be true singleton objects, 
    MyClass itself is a function, not a class, so you cannot call class methods from it. 
    Also for m = MyClass(); n = MyClass(); o = type(n)(); then m == n && m != o && n != o
"""
# ========================================================================
# 方法二：A Base Class

class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


class MyClass(Singleton):
    pass
"""
Pros

    It's a true class
Cons

    Multiple inheritance - eugh! __new__ could be overwritten during inheritance 
    from a second base class? One has to think more than is necessary.
"""


# ========================================================================

# 方法三：元类实现
class Singleton:
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(metaclass=Singleton):
    pass

"""
Pros

    It's a true class
    Auto-magically covers inheritance
    Uses __metaclass__ for its proper purpose (and made me aware of it)
"""

# ========================================================================

Method 4: decorator returning a class with the same name
def singleton(class_):
    class class_w(class_):
        _instance = None
        def __new__(class_, *args, **kwargs):
            if class_w._instance is None:
                class_w._instance = super(class_w,
                                    class_).__new__(class_,
                                                    *args,
                                                    **kwargs)
                class_w._instance._sealed = False
            return class_w._instance
        def __init__(self, *args, **kwargs):
            if self._sealed:
                return
            super(class_w, self).__init__(*args, **kwargs)
            self._sealed = True
    class_w.__name__ = class_.__name__
    return class_w

@singleton
class MyClass(BaseClass):
    pass

"""
    Pros

It's a true class
Auto-magically covers inheritance
Cons

    Is there not an overhead for creating each new class? Here we are creating two classes for 
    each class we wish to make a singleton. While this is fine in my case, I worry that this 
    might not scale. Of course there is a matter of debate as to whether it aught to be too easy 
    to scale this pattern...

    What is the point of the _sealed attribute

    Can't call methods of the same name on base classes using super() because they will recurse. 
    This means you can't customize __new__ and can't subclass a class that needs you to call up 
    to __init__.
"""