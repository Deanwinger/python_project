# 函数装饰器和闭包


##### 本章包含以下话题:
- Python 如何计算装饰器句法
- Python 如何判断变量是不是局部的
- 闭包存在的原因和工作原理
- nonlocal 能解决什么问题
- 实现行为良好的装饰器
- 标准库中有用的装饰器
- 实现一个参数化装饰器

## 7.1 装饰器基础知识
1. 语法糖解释
~~~
    @decorate
    def target():
        print('running target()')

    上述代码与下述写法一样:
    def target():
        print('running target()')
    target = decorate(target)
~~~

## 7.2 python何时执行装饰器
- 函数装饰器在导入模块时立即执行,而被装饰的函数只在明确调用时运行
~~~
示例 7-2 值的一看
~~~

## 7.3 使用装饰器改进"策略"模式
- 需结合第六章看


## 7.4 变量作用域规则
- nothing new

## 7.5 闭包
1. 举例:
~~~
背景: 在 averager 函数中,series 是自由变量(free variable)。这是一个技术术语,指未在本地作用域中绑定的变量

def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager

(1).审查返回的 averager 对象,我们发现 Python 在__code__ 属性(表示编译后的函数定义体)中保存局部变量和自由变量的名称:
>>> avg.__code__.co_varnames
('new_value', 'total')
>>> avg.__code__.co_freevars
('series',)

(2)series 的绑定在返回的 avg 函数的 __closure__ 属性中:
>>> avg.__closure__
(<cell at 0x107a44f78: list object at 0x107a91a48>,)
>>> avg.__closure__[0].cell_contents
[10, 11, 12]
~~~
2. 总结:
闭包是一种函数,它会保留定义函数时存在的自由变量的绑定,这样调用函数时,虽然定义作用域不可用了,但是仍能使用那些绑定。

## 7.6 nonlocal声明
