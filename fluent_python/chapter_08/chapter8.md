# 对象引用、可变性和垃圾回收

## 8.1 变量不盒子

## 8.2 标识、相等性和别名
1. 每个变量都有标示、值和类型， 对象一旦创建， 标示不会变（可以理解为对象在内存中的地址），is运算符比较两个对象的标识； id()函数返回对象标识的整数表示。

2. == 比较的是两个对象的值（对象中保存的数据）， 而is比较对象的标识， 再变量和单例值之间的比较时， 应该用is， is运算符比==速度快。

## 8.3 默认做浅复制
1. 复制列表(或多数内置的可变集合)最简单的方式是使用内置的类型构造方法，构造方法或 [:] 做的是浅复制(即复制了最外层容器,副本中的元素是源容器中元素的引用)。

2. == 比较的是两个对象的值（对象中保存的数据）， 而is比较对象的标识， 再变量和单例值之间的比较时， 应该用is， is运算符比==速度快。

## 8.4 函数的参数作为引用时
- `Python 唯一支持的参数传递模式是共享传参`

~~~
    共享传参指函数的各个形式参数获得实参中各个引用的副本。也就是说,(参数传递只是给对象绑定了一个新的变量)函数内部的形参是实参的别名。
~~~

### 8.4.1 不要使用可变类型作为参数的默认值
- P360的例子8-12非常值得一看
- 上例总结：
~~~
    self.passengers 变成了 passengers 参数默认值的别名。
    出现这个问题的根源是,默认值在定义函数时计算(通常在加载模块时),因此默认值变成了函数对象的属性。因此默认值变成了函数对象的属性。因此,如果默认值是可变对象,而且修改了它的值,那么后续的函数调用都会受到影响。
~~~

### 8.4.1 不要使用可变类型作为参数的默认值
### 8.4.2 防御可变参数

## 8.5 del和垃圾回收
- del 语句删除名称,而不是对象， 仅当删除的变量保存的是对象的最后一个引用时，或者无法得到对象时，导致对象被销毁；
- 在 CPython 中,垃圾回收使用的主要算法是引用计数,每个对象都会统计有多少引用指向自己，对象的引用计数为零时，对象立即就被销毁:
~~~
    cpython 会在对象上调用__del__方法（如果定义了）， 然后释放对象内存，如果除了循环引用之外没有其他引用,两个对象都会被销毁。
~~~

## 8.6 弱引用
- 弱引用不会增加对象的引用数量， 因此,弱引用不会妨碍所指对象被当作垃圾回收。

- 弱引用在缓存应用中很有用

- Python 控制台会自动把 _ 变量绑定到结果不为 None 的表达式结果上。

### 8.6.1 WeakValueDictionary简介
- to be finished

### 8.6.2 弱引用的局限
- 不是每个 Python 对象都可以作为弱引用的目标(或称所指对象)。基本的 list 和 dict 实例不能作为所指对象,但是它们的子类可以轻松地解决这个问题；

- int 和 tuple 实例不能作为弱引用的目标,甚至它
们的子类也不行；

- 这些局限基本上是 CPython 的实现细节,在其他 Python 解释器中情况可能不一样。

## 8.7 Python对不可变类型施加的把戏
- t[:] 不创建副本,而是返回同一个对象的引用。