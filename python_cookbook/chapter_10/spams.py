"""
当使用’from module import *’ 语句时, 定义一个变量 __all__ 来明确地列出需要导出的内容
"""

class spam(object):
    def bar(self):
        print('Hi, I am bar')

    def grok(self):
        print('Hi, I am grok')

def foo():
    print('Hi, I am foo')

__all__ = ['foo', 'spam'] 