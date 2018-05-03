# 符合Python风格的对象


##### 本章包含以下话题:
- 支持用于生成对象其他表示形式的内置函数(如repr()、bytes(),等等)
- 使用一个类方法实现备选构造方法
- 扩展内置的 format() 函数和 str.format() 方法使用的格式微语言
- 实现只读属性
- 把对象变为可散列的,以便在集合中及作为dict的键使用利用 __slots__ 节省内存

## 9.1 对象表示形式
1. 获取对象的字符串表现形式
~~~
repr()
  以便于开发者理解的方式返回对象的字符串表示形式。
str()
  以便于用户理解的方式返回对象的字符串表示形式
~~~

## 9.2 再谈向量类
 - 见文件vector2d_v0.py

## 9.3 备选构造方法
 - A Alternative Constructor

## 9.4 classmethod与staticmethod
1. classmethod: 定义，操作类而不是操作实例的方法。classmethod改变了调用方法的方式,因此类方法的第一个参数是类本身,而不是实例。classmethod最常见的用途是定义备选构造方法。见P392示例
2. staticmethod装饰器也会改变方法的调用方式,但是第一个参数不是特殊的值。其实,静态方法就是普通的函数,只是碰巧在类的定义体中,而不是在模块层定义。

## 9.5 格式化显示
1. 内置的 format() 函数和 str.format() 方法把各个类型的格式化方式委托给相应的 .__format__(format_spec) 方法。format_spec 是格式说明符,它是:
    - format(my_obj, format_spec) 的第二个参数,或者
    - str.format() 方法的格式字符串,{} 里代换字段中冒号后面的部分
~~~
>>> brl = 1/2.43 # BRL到USD的货币兑换比价
>>> brl
0.4115226337448559
>>> format(brl, '0.4f')
'0.4115'
>>> '1 BRL = {rate:0.2f} USD'.format(rate=brl)
'1 BRL = 0.41 USD'
~~~
2. 如果类没有定义 `__format__` 方法,从 object 继承的方法会返回str(my_object), 然而,如果传入格式说明符,`object.__format__` 方法会抛出TypeError

## 9.6 可散列的Vector2d
1. 可散列
  - 为了把 Vector2d 实例变成可散列的,必须使用 `__hash__` 方法，还需要 `__eq__` 方法, 为此,我们要把vector.x 和 vector.y 分量设为只读特性








######P395 to be finished