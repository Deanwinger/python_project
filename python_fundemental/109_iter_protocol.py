# 用__iter__和__next__方法，实现一个range方法
# 参考 fluent python 第十四章

# 序列可迭代的原因, iter函数 fluent python 14.1, 
# 简单点说就是: 解释器需要迭代对象时, 会自动调用iter(x), 如果有, 
# 就调用获取迭代器, 如果没有,但是有__getitem__, 会创建一个迭代器, 尝试按索引顺序获取元素;

# 要点: python 从可迭代对象中获取迭代器
# 可迭代对象: (14.2篇头有定义)两个要点: __iter__方法. __getitem__方法;
# 迭代器: (14.2篇尾有定义)标准的迭代器接口有两个方法, 实现了__iter__方法, 所以迭代器是可迭代的, __next__方法, 返回序列中的下一个元素;
# 生成器是迭代器

# 14.3章 看不太懂; to be finishded
# 可参考14.8 等差数列生成器


class MyRange:
    def __init__(self, begin, end=None, step=1):
        if end is None:
            self.begin = 0
            self.end = begin
        else:
            self.begin = begin
            self.end = end
        self.step = step

    # def __iter__(self):
        # x = self._elem
        # t = 0
        # while x > t:
        #     yield t
        #     t += 1
        # return
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.begin < self.end:
            ret = self.begin
            self.begin += self.step
            return ret
        raise StopIteration()

# 上述方法, 应该来说, 非常的不pythonic
class ArithmeticProgression:
    def __init__(self, begin, end=None, step=1):
        if end is None:
            self.begin = 0
            self.end = begin
        else:
            self.begin = begin
            self.end = end
        self.step = step

    def __iter__(self):
        result = self.begin
        while result < self.end:
            yield result
            result += self.step



if __name__ == '__main__':
    # g = myrange = MyRange(5)
    # g = myrange = MyRange(2,5)
    # l = range(2, 5)
    g = myrange = MyRange(2, 10, 3)
    l = range(2, 10, 3) 

    # 不支持   
    # g = myrange = MyRange(10, 0 -1)
    # l = range(10, 0, -1) 

    # g = myrange = MyRange(3, 3)
    # l = range(3, 3)    
    
    # print(list(g))
    # print(list(l))

    s = ArithmeticProgression(2, 10, 3)
    print(list(s))

