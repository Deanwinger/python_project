# Python Fundation

## Questions
- 参考1 
- 参考2 `https://github.com/taizilongxu/interview_python#1-python%E7%9A%84%E5%87%BD%E6%95%B0%E5%8F%82%E6%95%B0%E4%BC%A0%E9%80%92`
- 参考3 `https://zhuanlan.zhihu.com/auxten`
- 参考4 `https://zhuanlan.zhihu.com/p/21856569`

#### **1. 手写：正则邮箱地址**

- ^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$

#### **2. 可变与不可变类型**

- 可变: 
    - list, dict, 如果要进一步, bytearray,memoryview, array.array, collection.deque(待了解)
    ~~~
        dict 的变种(Fluent Python 3.5):
            (1). collections.OrderedDict: 这个类型在添加键的时候会保持顺序

            (2). collections.ChainMap: 该类型可以容纳数个不同的映射对象,然后在进行键查找操作的时候,
                 这些对象会被当作一个整体被逐个查找,直到键被找到为止。

            (3). collections.Counter: 这个映射类型会给键准备一个整数计数器。每次更新一个键的时候
                 都会增加这个计数器。所以这个类型可以用来给可散列表对象计数.

            (4). colllections.UserDict: 这个类其实就是把标准 dict 用纯 Python 又实现了一遍, UserDict 是让用户继承写子类的
    ~~~

- 不可变:
    - tuple, str, bytes

#### **3. Python是如何进行内存管理的**
`http://www.cnblogs.com/CBDoctor/p/3781078.html` -- 此文章非常值得一读
- 从三个方面来说,一对象的引用计数机制,二垃圾回收机制,三内存池机制
>1. 对象的引用计数机制

~~~
    python内部使用引用计数，来保持追踪内存中的对象，所有对象都有引用计数。

    引用计数增加的情况：

        1，一个对象分配一个新名称

        2，将其放入一个容器中（如列表、元组或字典）

    引用计数减少的情况：

        1，使用del语句对对象别名显示的销毁

        2，引用超出作用域或被重新赋值

    sys.getrefcount( )函数可以获得对象的当前引用计数

    多数情况下，引用计数比你猜测得要大得多。对于不可变数据（如数字和字符串），解释器会在程序的不同部分共享内存，以便节约内存。

二、垃圾回收
`参考第88题`
    1，当一个对象的引用计数归零时，它将被垃圾收集机制处理掉。

    2，当两个对象a和b相互引用时，del语句可以减少a和b的引用计数，并销毁用于引用底层对象的名称。然而由于每个对象都包含一个对其他对象的应用，因此引用计数不会归零，对象也不会销毁。（从而导致内存泄露）。为解决这一问题，解释器会定期执行一个循环检测器，搜索不可访问对象的循环并删除它们。

三、内存池机制

    Python提供了对内存的垃圾收集机制，但是它将不用的内存放到内存池而不是返回给操作系统。

    1，Pymalloc机制。为了加速Python的执行效率，Python引入了一个内存池机制，用于管理对小块内存的申请和释放。

    2，Python中所有小于256个字节的对象都使用pymalloc实现的分配器，而大的对象则使用系统的malloc。

    3，对于Python对象，如整数，浮点数和List，都有其独立的私有内存池，对象间不共享他们的内存池。也就是说如果你分配又释放了大量的整数，用于缓存这些整数的内存就不能再分配给浮点数。
~~~

#### **4. 可迭代对象, 迭代器, 生成器**

`Fluent Python 第14章: 可迭代的对象, 迭代器和生成器`

- 迭代是数据处理的基石

>1. 可迭代对象
- 使用 iter 内置函数可以获取迭代器的对象。如果对象实现了能返回迭代器的 __iter__ 方法,那么对象就是可迭代的。序列都可以迭代;实现了 __getitem__ 方法,而且其参数是从零开始的索引,这种对象也可以迭代。
~~~
序列可以迭代的原因:
    iter函数,解释器需要迭代对象 x 时,会自动调用 iter(x), 内置的 iter 函数有以下作用:
        (1) 检查对象是否实现了 __iter__ 方法,如果实现了就调用它,获取一个迭代器。
        (2) 如果没有实现 __iter__ 方法,但是实现了 __getitem__ 方法,Python 会创建一个迭代器,
            尝试按顺序(从索引 0 开始)获取元素。
        (3) 如果尝试失败,Python 抛出 TypeError 异常,会提示“C object is not iterable”(C 对象不可迭代),
            其中 C 是目标对象所属的类。
~~~

>2. 迭代器
- 可迭代的对象和迭代器之间的关系:Python 从可迭代对象中获取迭代器。

- 迭代器:实现了无参数的 __next__ 方法,返回序列中的下一个元素;如果没有元素了,那么抛出 StopIteration 异常。Python 中的迭代器还实现了 __iter__ 方法,因此迭代器也可以迭代。
~~~
    标准的迭代器接口有两个方法。
        __next__
        返回下一个可用的元素,如果没有元素了,抛出 StopIteration异常;

        __iter__
        返回 self,以便在应该使用可迭代对象的地方使用迭代器,例如在 for 循环中;
~~~

>3. 生成器
- Python有两种不同的方式提供生成器:
~~~
    1. 生成器表达式
    2. 生成器函数: 使用 yield 关键字的函数或方法; 调用生成器函数返回的是生成器对象; 跟普通函数不同的是，生成器只能用于迭代操作;

    - 根据我的经验,选择使用哪种句法:如果生成器表达式要分成多行写,我倾向于定义生成器函数,以便提高可读性。此外,生成器函数有名称,因此可以重用。
~~~
- 语法解释
~~~
    (1). 语法上和函数类似：生成器函数和常规函数几乎是一样的。它们都是使用def语句进行定义，差别在于，
         生成器使用yield语句返回一个值，而常规函数使用return语句返回一个值
    (2). 自动实现迭代器协议：对于生成器，Python会自动实现迭代器协议，以便应用到迭代背景中（如for循环）。
         由于生成器自动实现了迭代器协议，所以，我们可以调用它的next方法，在没有值可以返回的时候，生成器自动产生StopIteration异常状态
    (3). 挂起：生成器使用yield语句返回一个值。yield语句挂起该生成器函数的状态，保留足够的信息，
         以便之后从它离开的地方继续执行
~~~
#### **5. 介绍下装饰器**
`Fluent Python 第七章`
`https://www.zhihu.com/question/25950466`
`https://stackoverflow.com/questions/739654/how-to-make-a-chain-of-function-decorators`
>1. 装饰器的一大特性是,能把被装饰的函数替换成其他函数。第二个特性是,装饰器在加载模块时立即执行
>2. 多数装饰器会修改被装饰的函数。通常,它们会定义一个内部函数,然后将其返回,替换被装饰的函数。使用内部函数的代码几乎都要靠闭包才能正确运作。
>3. 为了理解闭包,我们要退后一步,先了解 Python中的变量作用域--LEGB,同时`参考54题`
~~~
    import time
    def clock(func):
        def clocked(*args):
            t0 = time.time()
            result = func(*args)
            elapsed = time.time() - t0
            print("Total running time is: ", elapsed)
            return result
        return clocked

    @clock
    def factorial(n):
        return 1 if n < 2 else n*factorial(n-1)

    等价于
    def factorial(n):
        return 1 if n < 2 else n*factorial(n-1)

    factorial = clock(factorial)

    clock 装饰器有几个缺点:不支持关键字参数,而且遮盖了被装饰函数的 __name__ 和 __doc__ 属性

    改进后的 clock 装饰器

    import time
    import functools
    
    def clock(func):
        @functools.wraps(func)
        def clocked(*args, **kwargs):
            t0 = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - t0
            print("Total running time is: ", elapsed)
            return result
        return clocked
~~~

- 叠放的装饰器
~~~
    @d1
    @d2
    def f():
        print('f')

    等同于:

    def f():
        print('f')

    f = d1(d2(f))
~~~

#### **6. 以装饰器的方式实现单例模式,使用装饰器的单例和使用其他方法的单例，在后续使用中，有何区别**
`http://python-web-guide.readthedocs.io/zh/latest/design/design.html#id1`
- 上面总结的很好了
- 参考singleton.py, 上面有总结

#### **7. 写一个简单的python socket编程**
~~~
# 首先，创建一个基于IPv4和TCP协议的Socket：

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口,小于1024的端口号必须要有管理员权限才能绑定：
s.bind(('127.0.0.1', 9999))

#紧接着，调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
s.listen(5)
print('Waiting for connection...')

#接下来，服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

# 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

~~~

#### **8. 浅拷贝与深拷贝**
`Fluent Python第八章`
- 每个变量都有标识、类型和值。对象一旦创建,它的标识绝不会变;你可以把标识理解为对象在内存中的地址。is 运算符比较两个对象的标识;id() 函数返回对象标识的整数表示, 而变量名, 不过是给每个对象贴的标签;
~~~
    (1). 对象 ID 的真正意义在不同的实现中有所不同。在 CPython 中,id() 返回对象的内存地址,但是在其他 Python 解释器中可能是别的值。
    (2). is 运算符比 == 速度快,因为它不能重载,所以 Python 不用寻找并调用特殊方法,而是直接比较两个整数 ID
~~~

- Python 集合(列表、字典、元组,等等)一样,保存的是对象的引用;

- 默认做浅复制, 复制列表(或多数内置的可变集合)最简单的方式是使用内置的类型构造方法。
~~~
    浅拷贝：创建一个新的对象，但它包含的是对原始对象中包含项的引用（如果用引用的方式修改其中一个对象，另外一个也会修改改变）{1,完全切片方法；2，工厂函数，如list()；3，copy模块的copy()函数}
    
    深拷贝：创建一个新的对象，并且递归的复制它所包含的对象（修改其中一个，另外一个不会改变）{copy模块的deep.deepcopy()函数}
~~~

#### **9. 列表推导和生成器的优劣**

- 列表推导式一次性产生全部需要的值;
- 生成式是惰性求值, 而且只遍历一遍;

#### **10. 弱引用**
`Fluent Python 8.6 弱引用`


#### **11. 介绍下协程，为何比线程还快**
`Fluent Python 第16章`
`https://zhuanlan.zhihu.com/p/25228075`
- 协程就是你可以暂停执行的函数， 协程就是一种用户态内的上下文切换技术, 它是比是线程（thread）更细量级的用户态线程，特点是允许用户的主动调用和主动退出，挂起当前的例程然后返回值或去执行其他任务，接着返回原来停下的点继续执行。

- 从句法上看,协程与生成器类似,都是定义体中包含 yield 关键字的函数。可是,在协程中,yield 通常出现在表达式的右边(例如,data = yield),可以产出值,也可以不产出——如果 yield关键字后面没有表达式,那么生成器产出 None。协程可能会从调用方接收数据,不过调用方把数据提供给协程使用的是 .send(data) 方法,通常,调用方会把值推送给协程。


>16.1 生成器如何进化成协程
~~~
    生成器的调用方可以使用 .send(...) 方法发送数据,发送的数据会成为生成器函数中 yield 表达式的值。因此,生成器可以作为协程使用。协程是指一个过程,这个过程与调用方协作,产出由调用方提供的值。

    区别：
        generator总是生成值，一般是迭代的序列

        coroutine关注的是消耗值，是数据(data)的消费者

        coroutine不会与迭代操作关联，而generator会

        coroutine强调协同控制程序流，generator强调保存状态和产生数据


~~~

>16.2 用作协程的生成器的基本行为
~~~
    协程可以身处四个状态中的一个。当前状态可以使用inspect.getgeneratorstate(...) 函数确定,该函数会返回下述字
    符串中的一个: 

    'GEN_CREATED' -- 等待开始执行。
    
    'GEN_RUNNING' -- 解释器正在执行, 只有在多线程应用中才能看到这个状态。

    'GEN_SUSPENDED' -- 在 yield 表达式处暂停。
    
    'GEN_CLOSED' -- 执行结束。
~~~

>16.3 示例:使用协程计算移动平均值
~~~
    def averager():
        total = 0.0
        count = 0
        average = None

        while True:
            term = yield average
            total += term
            count += 1
            average = total / count
~~~

>16.4 预激协程的装饰器
~~~
    from functools import wraps

    def coroutine(func):
        """装饰器:向前执行到第一个`yield`表达式,预激`func`"""
        @wraps(func)
        def primer(*args,**kwargs):
            gen = func(*args,**kwargs) 
            next(gen) 
            return gen
        return primer
~~~

>16.5 终止协程和异常处理
>16.6 让协程返回值
~~~
    生成器对象会抛出 StopIteration 异常。异常对象的 value 属性保存着返回的值。

    return 表达式的值会偷偷传给调用方,赋值给 StopIteration异常的一个属性。这样做有点不合常理,但是能保留生成器对象的常规行为——耗尽时抛出 StopIteration 异常。
~~~

#### **12. 强类型/弱类型和静态类型/动态类型**

#### **13. Python中的多线程, 多进程**
`https://zhuanlan.zhihu.com/p/20167077`
`http://www.dongwm.com/archives/%E4%BD%BF%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B-asyncio%E7%AF%87/`
`http://www.dongwm.com/archives/%E4%BD%BF%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B-asyncio%E7%AF%87-%E4%BA%8C/`
`http://www.dongwm.com/archives/%E4%BD%BF%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B-asyncio%E7%AF%87-%E4%B8%89/`
- 再多线程编程中, 如果一个线程执行一个原子操作, 这意味着另一个线程无法看到该操作一半的结果, 系统只能处于操作之前或者是操作之后的状态, 而不能介于两者之间的状态;

- concurrent.futures
~~~
    ProcessPoolExecutor 和 ThreadPoolExecutor 类都实现了通用的Executor 接口,因此使用 concurrent.futures 模块能特别轻松地把基于线程的方案转成基于进程的方案。

    futures.ThreadPoolExecutor 类对某个作业来说不够灵活,可能要使用 threading 模块中的组件(如 Thread、Lock、Semaphore 等)自行制定方案; futures.ThreadPoolExecutor 类已经封装了这些组件

    对 CPU 密集型工作来说,要启动多个进程,规避 GIL。创建多个进程最简单的方式是,使用futures.ProcessPoolExecutor 类。不过和前面一样,如果使用场景较复杂,需要更高级的工具。multiprocessing 模块的 API 与threading 模块相仿,不过作业交给多个进程处理。不过,multiprocessing 模块还能解决协作进程遇到的最大挑战:在进程之间传递数据;
~~~

#### **14. python最常见的解释器**

#### **15. python中map, filter, reduce的使用**

- 在 Python 3 中,map 和 filter 都是内置函数, 返回生成器(一种迭代器),但是由于引入了列表推导和生成器表达式,它们变得没那么重要了。列表推导或生成器表达式具有 map 和 filter 两个函数的功能
~~~
    map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

    和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
~~~

- reduce
~~~
    1. 在 Python 2 中,reduce 是内置函数,但是在 Python 3 中放到functools 模块里了,reduce() 函数的第一个参数是接受两个参数的函数,第二个参数是一个可迭代的对象。假如有个接受两个参数的 fn 函数和一个 lst 列表。调用reduce(fn, lst) 时,fn 会应用到第一对元素上,即 fn(lst[0], lst[1]),生成第一个结果 r1。然后,fn 会应用到 r1 和下一个元素上,即 fn(r1, lst[2]),生成第二个结果 r2。接着,调用 fn(r2,lst[3]),生成 r3......直到最后一个元素,返回最后得到的结果 rN

    2. 使用reduce函数时最好提供第三个参数,reduce(function, iterable, initializer),这样能避免这个异常:TypeError: reduce() of empty sequence with no initial value(这个错误消息很棒,说明了问题,还提供
    了解决方法)。如果序列为空,initializer 是返回的结果;否则,在归约中使用它作为第一个参数,因此应该使用恒等值。
    比如,对 +、| 和 ^ 来说, initializer 应该是 0;而对 * 和 & 来说,应该是 1。
~~~

#### **16. 知道GIL的限制以及与多线程的关系**
`廖雪峰`
`Fluent Python 17.2 阻塞型I/O和GIL`
`Fluent Python 17.5.3 线程和多进程的替代方案`
- Python解释器被一个锁保护着, 只允许一次执行一个线程, 即使存在多个可用的处理器, 在计算密集型的应用中,严重的限制了线程的作用; 对于计算密集型的任务来说, 最好使用C拓展或者是multiprocessing模块来代替, C拓展有释放解释器锁和并行运算的选项, 前提是释放锁时, 不与解释器进行交互, multiprocessing模块将工作分给不受限制的单独子进程;

- GIL的释放逻辑是当前线程遇见IO操作或者计时器达到100（ticks可以看作是python自身的一个计数器，专门做用于GIL，每次释放后归零，这个计数可以通过 sys.setcheckinterval 来调整），进行释放。

#### **17. python中dict的底层实现，以及与OrderDict的关系, dict和UserDict的关系，为什么有UserDict的存在**
`Fluent Python 3.9--dict和set的背后`
- 散列表其实是一个稀疏数组(总是有空白元素的数组称为稀疏数组)。散列表里的单元通常叫作表元(bucket)。在 dict 的散列表当中,每个键值对都占用一个表元,每个表元都有两个部分,一个是对键的引用,另一个是对值的引用。Python 会设法保证大概还有三分之一的表元是空的,所以在快要达到这个阈值的时候,原有的散列表会被复制到一个更大的空间里面。

- 散列表算法:
~~~
为了获取 my_dict[search_key] 背后的值,Python 首先会调用hash(search_key) 来计算 search_key 的散列值,把这个值最低的几位数字当作偏移量,在散列表里查找表元(具体取几位,得看当前散列表的大小)。若找到的表元是空的,则抛出 KeyError 异
常。若不是空的,则表元里会有一对 found_key:found_value。这时候 Python 会检验 search_key == found_key 是否为真,如果它们相等的话,就会返回 found_value。

如果 search_key 和 found_key 不匹配的话,这种情况称为散列冲突。发生这种情况是因为,散列表所做的其实是把随机的元素映射到只有几位的数字上,而散列表本身的索引又只依赖于这个数字的一部分。为了解决散列冲突,算法会在散列值中另外再取几位,然后用特殊的方法处理一下,把新得到的数字再当作索引来寻找表元。 若这次找到的表元是空的,则同样抛出 KeyError;若非空,或者键匹配,则返回这个值;或者又发现了散列冲突,则重复以上的步骤。
~~~

- 优势和限制:
~~~
    (1). 键必须是可散列的, 一个可散列的对象必须满足以下要求:
        a. 支持 hash() 函数,并且通过 __hash__() 方法所得到的散列值是不变的。
        b. 支持通过 __eq__() 方法来检测相等性。
        c. 若 a == b 为真,则 hash(a) == hash(b) 也为真。
    (2). 字典在内存上的开销巨大
    (3). 键查询很快
~~~

- 与OrderDict的关系：

~~~
    collections.OrderedDict
    这个类型在添加键的时候会保持顺序,因此键的迭代次序总是一致的。OrderedDict 的 popitem 方法默认删除并返回的是字典里的最后一个元素,但是如果像 my_odict.popitem(last=False) 这样调用它,那么它删除并返回第一个被添加进去的元素

    返回按key排序后的字典L:
     OrderedDict(sorted(a.items(),key=lambda x: x[0]))
~~~

- 与UserDict关系
`fluent python 3.1--3.6, 12.1`
~~~
    创造自定义映射类型来说,以 UserDict 为基类,总比以普通的dict 为基类要来得方便;
    更倾向于从 UserDict 而不是从 dict 继承的主要原因是,后者有时会在某些方法的实现上走一些捷径,导致我们不得不在它的子类中重写这些方法,但是 UserDict 就不会带来这些问题;
~~~

#### **18. python多继承的查找规则（MRO）**
`Fluent Python 第12章--继承的优缺点`
`http://www.cnblogs.com/lovemo1314/archive/2011/05/03/2035005.html`

- Python 会按照特定的顺序遍历继承图。这个顺序叫方法解析顺序(Method Resolution Order,MRO)。类都有一个名为 __mro__ 的属性,它的值是一个元组,按照方法解析顺序列出各个超类,从当前类一直向上,直到object 类。

- 内置的 super() 函数会按照__mro__ 属性给出的顺序调用超类的方法; super 指的是 MRO 中的下一个类！


#### **19. property的含义以及其描述器实现**
`Fluent Python 19.2`

#### **20. __slots__的含义以及使用场景**
`Fluent Python 9.8 使用 __slots__ 类属性节省空间`
- 默认情况下,Python 在各个实例中名为 __dict__ 的字典里存储实例属性。如 3.9.3 节所述,为了使用底层的散列表提升访问速度,字典会消耗大量内存。如果要处理数百万个属性不多的实例,通过 __slots__类属性,能节省大量内存,方法是让解释器在元组中存储实例属性,而不用字典。

- 在类中定义 __slots__ 属性的目的是告诉解释器:“这个类中的所有实例属性都在这儿了!”这样,Python 会在各个实例中使用类似元组的结构存储实例变量,从而避免使用消耗内存的 __dict__ 属性。如果有数百万个实例同时活动,这样做能节省大量内存。
~~~
    tips:
        1. 继承自超类的 __slots__ 属性没有效果。Python 只会使用各个类中定义的 __slots__ 属性;
        2. 实例只能拥有 __slots__ 中列出的属性, 除非把 '__dict__' 加入 __slots__ 中(这样做就失去了节省内存的功效);
        3. 如果不把 '__weakref__' 加入 __slots__,实例就不能作为弱引用的目标;
~~~

#### **21. 如何定义和使用元类，了解其使用场景**
`http://blog.jobbole.com/21351/`
- 在Python中，类也是对象，你可以动态的创建类。函数type实际上是一个元类。type就是Python在背后用来创建所有类的元类;
~~~
    1. type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
    MyShinyClass = type('MyShinyClass', (), {})  # 返回一个类对象
~~~
- 元类就是用来创建类的“东西”。你创建类就是为了创建类的实例对象，不是吗？但是我们已经学习到了Python中的类也是对象。好吧，元类就是用来创建这些类（对象）的，元类就是类的类;

~~~
    __metaclass__属性

    你可以在写一个类的时候为其添加__metaclass__属性。如果你这么做了，Python就会用元类来创建类Foo。小心点，这里面有些技巧。你首先写下class Foo(object)，但是类对象Foo还没有在内存中创建。Python会在类的定义中寻找__metaclass__属性，如果找到了，Python就会用它来创建类Foo，如果没有找到，就会用内建的type来创建这个类。

    2. 当写下如下代码时:
    class Foo(Bar):
        pass
    Python做了如下的操作：

    Foo中有__metaclass__这个属性吗？如果是，Python会在内存中通过__metaclass__创建一个名字为Foo的类对象（我说的是类对象，请紧跟我的思路）。它就会在模块层次中去寻找__metaclass__，并尝试做同样的操作。如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象。
    现在的问题就是，你可以在__metaclass__中放置些什么代码呢？答案就是：可以创建一个类的东西。那么什么可以用来创建一个类呢？type，或者任何使用到type或者子类化type的东东都可以。
~~~

- 但就元类本身而言，它们其实是很简单的：
~~~
    1)   拦截类的创建

    2)   修改类

    3)   返回修改之后的类
~~~


#### **22. python中type和object之间的关系**

#### **23. python中的打包方式（setup.py）**
`Python高级编程 第五章--编写一个包`

#### **24. PEP8常见的范式,至少列举5个**
- Style Guide for Python Code
~~~
    一 代码编排
        1 缩进。4个空格的缩进（编辑器都可以完成此功能），不使用Tap，更不能混合使用Tap和空格。
        2 每行最大长度79，换行可以使用反斜杠，最好使用圆括号。换行点要在操作符的后边敲回车。
        3 类和top-level函数定义之间空两行；类中的方法定义之间空一行；函数内逻辑无关段落之间空一行；其他地方尽量不要再空行。

    二 文档编排
        1 模块内容的顺序：模块说明和docstring—import—globals&constants—其他定义。其中import部分，又按标准、三方和自己编写顺序依次排放，之间空一行。
        2 不要在一句import中多个库，比如import os, sys不推荐。
        3 如果采用from XX import XX引用库，可以省略‘module.’，都是可能出现命名冲突，这时就要采用import XX。

    三 空格的使用
        总体原则，避免不必要的空格。
        1 各种右括号前不要加空格。
        2 逗号、冒号、分号前不要加空格。
        3 函数的左括号前不要加空格。如Func(1)。
        4 序列的左括号前不要加空格。如list[2]。
        5 操作符左右各加一个空格，不要为了对齐增加空格。
        6 函数默认参数使用的赋值符左右省略空格。
        7 不要将多句语句写在同一行，尽管使用‘；’允许。
        8 if/for/while语句中，即使执行语句只有一句，也必须另起一行。

    四 注释
        总体原则，错误的注释不如没有注释。所以当一段代码发生变化时，第一件事就是要修改注释！
        注释必须使用英文，最好是完整的句子，首字母大写，句后要有结束符，结束符后跟两个空格，开始下一句。如果是短语，可以省略结束符。
        1 块注释，在一段代码前增加的注释。在‘#’后加一空格。段落之间以只有‘#’的行间隔。比如：
        # Description : Module config.
        # 
        # Input : None
        #
        # Output : None
        2 行注释，在一句代码后加注释。比如：x = x + 1	# Increment x
        但是这种方式尽量少使用。
        3 避免无谓的注释。

    五 文档描述
        1 为所有的共有模块、函数、类、方法写docstrings；非共有的没有必要，但是可以写注释（在def的下一行）。
        2 如果docstring要换行，参考如下例子,详见PEP 257
        """Return a foobang

        Optional plotz says to frobnicate the bizbaz first.

        """

    六 命名规范
        总体原则，新编代码必须按下面命名风格进行，现有库的编码尽量保持风格。
        1 尽量单独使用小写字母‘l’，大写字母‘O’等容易混淆的字母。
        2 模块命名尽量短小，使用全部小写的方式，可以使用下划线。
        3 包命名尽量短小，使用全部小写的方式，不可以使用下划线。
        4 类的命名使用CapWords的方式，模块内部使用的类采用_CapWords的方式。
        5 异常命名使用CapWords+Error后缀的方式。
        6 全局变量尽量只在模块内有效，类似C语言中的static。实现方法有两种，一是__all__机制;二是前缀一个下划线。
        7 函数命名使用全部小写的方式，可以使用下划线。
        8 常量命名使用全部大写的方式，可以使用下划线。
        9 类的属性（方法和变量）命名使用全部小写的方式，可以使用下划线。
        9 类的属性有3种作用域public、non-public和subclass API，可以理解成C++中的public、private、protected，non-public属性前，前缀一条下划线。
        11 类的属性若与关键字名字冲突，后缀一下划线，尽量不要使用缩略等其他方式。
        12 为避免与子类属性命名冲突，在类的一些属性前，前缀两条下划线。比如：类Foo中声明__a,访问时，只能通过Foo._Foo__a，避免歧义。如果子类也叫Foo，那就无能为力了。
        13 类的方法第一个参数必须是self，而静态方法第一个参数必须是cls。
~~~

#### **25. 鸭子类型（duck typing）的含义与其在python中的表现形式**
`Fluent Python 10.3 协议和鸭子类型`
- “鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子;

- 对象的类型无关紧要, 只要实现了特定的协议即可(协议是非正式的接口), 例如,Python 的序列协议只需要 __len__ 和 __getitem__ 两
个方法。任何类(如 Spam),只要使用标准的签名和语义实现了这两个方法,就能用在任何期待序列的地方。


#### **26. Python dict的顺序**

#### **27. python中重载**
~~~
    函数重载主要是为了解决两个问题。

    可变参数类型。
    可变参数个数。
    另外，一个基本的设计原则是，仅仅当两个函数除了参数类型和参数个数不同以外，其功能是完全相同的，此时才使用函数重载，如果两个函数的功能其实不同，那么不应当使用重载，而应当使用一个名字不同的函数。

    好吧，那么对于情况 1 ，函数功能相同，但是参数类型不同，python 如何处理？答案是根本不需要处理，因为 python 可以接受任何类型的参数，如果函数的功能相同，那么不同的参数类型在 python 中很可能是相同的代码，没有必要做成两个不同函数。

    那么对于情况 2 ，函数功能相同，但参数个数不同，python 如何处理？大家知道，答案就是缺省参数。对那些缺少的参数设定为缺省参数即可解决问题。因为你假设函数功能相同，那么那些缺少的参数终归是需要用的。

    好了，鉴于情况 1 跟 情况 2 都有了解决方案，python 自然就不需要函数重载了。
~~~

#### **28. 如何利用collections，itertools，operator等模块来高效地操作容器对象。**
`问题太大, pass`

#### **29. python中序列化的常用库和接口（json，pickle）**
`廖雪峰 + Python 参考手册`
- 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上; 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

- 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便, JSON表示的对象就是标准的JavaScript语言的对象，

#### **30. StringIO和BytesIO的用途。**
`廖雪峰 -- IO 编程`
- 很多时候，数据读写不一定是文件，也可以在内存中读写, StringIO顾名思义就是在内存中读写str。
- StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO, BytesIO实现了在内存中读写bytes;

#### **31. 单下划线开头、双下划线开头和双下划线包围的变量分别代表着什么含义**
`Fluent Python 9.7 Python的私有属性和“受保护的”属性`
~~~
    a. Python内置的“魔法”方法或属性, 你也可以自己定义，但一般不推荐:
        __name__：一种约定，Python内部的名字，用来与用户自定义的名字区分开，防止冲突
    
    b. 内部使用的变量、属性、方法、函数、类或模块（约定）, from foo import * 不会导入以下划线开头的对象
        _name：一种约定，用来指定变量私有, 不会阻止外部的访问
    
    c. 类外部无法直接使用原名称访问, 需要通过instance._ClassName__var的形式访问
        __name：解释器用_classname__name来代替这个名字用以区别和其他类相同的命名
~~~

#### **32. __init__和__new__方法在class和type中分别的作用是什么**
`https://zhuanlan.zhihu.com/p/35943253`
~~~
    __new__() 用于创建实例, 注意方法的第一个参数是cls(类本身)
    __init__() 用于初始化对象的属性, 再创建对象后马上调用;
~~~

#### **33. 类变量和实例变量的区别**

#### **34. __dict__在类中的含义，以及类属性和方法与__dict__的关系**
`Fluent Python 5.6 函数内省`
- __dict__属性用于存储与一个实例相关的所有数据
~~~
__dict__与dir()的区别：

dir()是一个函数，返回的是list；
__dict__是一个字典，键为属性名，值为属性值；
dir()用来寻找一个对象的所有属性，包括__dict__中的属性，__dict__是dir()的子集；
​ 并不是所有对象都拥有__dict__属性。许多内建类型就没有__dict__属性，如list，此时就需要用dir()来列出对象的所有属性。
~~~

#### **35. python的模块间循环引用的问题，如何避免它**

#### **36. python中抽象类的实现方式，以及其抽象基类模块，如何用python类实现一个抽象容器类型。**
`Fluent Python 第 11 章`
- collections.abc 模块中定义了 16 个抽象基类(Python 标准库的numbers 模块中还有一些);
~~~
    1. 想实现子类,我们可以覆盖从抽象基类中继承的方法;
        a. 抽象容器类, 需要实现 -- __contains__、__iter__、__len__, Container
        b. Iterable 通过 __iter__ 方法支持迭代,Container 通过__contains__ 方法支持 in 运算符,Sized 通过 __len__ 方法支持len() 函数
~~~

`Fluent Python 11.7 定义并使用一个抽象基类`
- to be finished

#### **37. classmethod和staticmethod的区别**
`Fluent Python 9.4 classmethod与staticmethod`
- classmethod
~~~
    用法:定义操作类,而不是操作实例的方法。classmethod 改变了调用方法的方式,因此类方法的第一个参数是类本身,而不是实例。classmethod 最常见的用途是定义备选构造方法
~~~

- staticmethod 
~~~
    静态方法就是普通的函数,只是碰巧在类的定义体中,而不是在模块层定义
~~~

#### **38. 装饰器中添加functools.wraps的含义与作用**
- functools.wraps 则可以将原函数对象的属性复制给包装函数, 默认有 __module__、__name__、__doc__

#### **39. __getattr__和__getattribute__的作用以及其顺序关系**
`Fluent Python 10.5--动态存取属性, 第19章--动态属性和特性, 19.6.3--处理属性的特殊方法`
- __getattr__
- 
~~~
    __getattr__(self, name)
    仅当获取指定的属性失败,搜索过 obj、Class 和超类之后调用。表达式 obj.no_such_attr、getattr(obj, 'no_such_attr') 和hasattr(obj, 'no_such_attr') 可能会触发Class.__getattr__(obj, 'no_such_attr') 方法,但是,仅当在obj、Class 和超类中找不到指定的属性时才会触发。

    __getattribute__(self, name)
    尝试获取指定的属性时总会调用这个方法,不过,寻找的属性是特殊属性或特殊方法时除外。点号与 getattr 和 hasattr 内置函数会触发这个方法。调用 __getattribute__ 方法且抛出 AttributeError异常时,才会调用 __getattr__ 方法。为了在获取 obj 实例的属性时不导致无限递归,__getattribute__ 方法的实现要使用
    super().__getattribute__(obj, name)。
~~~

#### **40. python中性能测量的方式，如cProfile，tracemalloc**

#### **41. python中自省的使用方式**
`Fluent Python 5.8 获取关于参数的信息`
- 自省就是面向对象的语言所写的程序在运行时，所能知道对象的类型。简单一句话就是运行时能够获得对象的类型, Python 附带一些内置函数和模块来帮助我们检查这些对象, 比如：type()、dir()、getattr()、hasattr()、isinstance()；
~~~
    一.
    1. dir 是内省最重要的函数之一，它返回一个对象的属性和方法列表;
    2. type 函数返回一个对象的类型;
    3. id 函数返回各种对象的唯一 id
    二. 
    1. inspect模块
~~~

#### **42. sys.settrace和sys.setprofile在python中的用途和使用方式**

#### **43. python中的模块定义，以及导入模块的各种姿势**
`https://juejin.im/entry/570c6b6771cfe40067310370`

#### **44. global和nonlocal关键字在python中的含义和其使用场景**
`Fluent Python 7.4 变量作用域规则`
~~~
    nonlocal 声明。它的作用是把变量标记为自由变量,即使在函数中为变量赋予新值了,也会变成自由变量。
~~~

#### **45. for-else，try-else的含义和用途**
`Python参考手册`

#### **46. .pyc文件的含义，清楚python代码大概的执行过程**

#### **47. python中格式化字符串的方式以及其常见格式语法**
`印象笔记的收藏`
>1. %-格式化

>2. str.format()
~~~
    >>> name = "hoxis"
    >>> age = 18

    (1).
    >>> "hello, {}. you are {}?".format(name,age)
    'hello, hoxis. you are 18?'

    (2). 可以通过索引来以其他顺序引用变量：
    >>> "hello, {1}. you are {0}?".format(age,name)
    'hello, hoxis. you are 18?'

    (3).
    >>> "hello, {name}. you are {age1}?".format(age1=age,name=name)
    'hello, hoxis. you are 18?'
~~~
>3. f-Strings
~~~
    (1).
    >>> f"hi, {name}, are you {age}"
    'hi, hoxis, are you 18'
    >>> F"hi, {name}, are you {age}"
    'hi, hoxis, are you 18'
~~~

#### **48. python中常见的魔术方法和其使用方式**
`Fluent Python 第一章 1.2`

#### **49. 描述符**
`Fluent Python 第二十章`
`http://www.dongwm.com/archives/%E6%B7%B1%E5%85%A5%E5%B1%9E%E6%80%A7%E6%8F%8F%E8%BF%B0%E7%AC%A6/`

#### **50. python递归的最大层数**
- python最大递归层数为1000层,通过setrecursionlimit函数来设置最大递归数, 以通过getrecursionlimit函数获取当前的递归层数

#### **51. *arg和**kwarg作用**
- 如果我们不确定往一个函数中传入多少参数，或者我们希望以元组（tuple）或者列表（list）的形式传参数的时候，我们可以使用*args（单星号）。如果我们不知道往函数中传递多少个关键词参数或者想传入字典的值作为关键词参数的时候我们可以使用**kwargs（双星号）

#### **52. **

#### **53. 正则的贪婪匹配**
`廖雪峰`

#### **54. 你对闭包的理解**
`Fluent Python 7.5 闭包`
- 简单来讲，一个闭包就是一个函数, 一个绑定了自由变量的函数， 只不过在函数内部带上了一个额外的变量环境。闭包关键特点就是它会记住自己被定义时的环境。

- 自由变量(free variable): 指未在本地作用域中绑定的变量

- 我们发现 Python 在 __code__ 属性(表示编译后的函数定义体)中保存局部变量和自由变量的名称, 实际值 绑定在返回函数 的 __closure__ 属性中
~~~
    示例：
    flist = []
    for i in range(3):
        def afunc(x):
            return x*i
    for f in flist:
        print(f(2))

    闭包最重要的使用价值在于：封存函数执行的上下文环境；
    闭包在其捕捉的执行环境(def语句块所在上下文)中，也遵循LEGB规则逐层查找，直至找到符合要求的变量，或者抛出异常

    当代码执行到show_filename中的return "filename: %s" % filename语句时，解析器按照下面的顺序查找filename变量：

    Local - 本地函数(show_filename)内部，通过任何方式赋值的，而且没有被global关键字声明为全局变量的filename变量；
    Enclosing - 直接外围空间(上层函数wrapper)的本地作用域，查找filename变量(如果有多层嵌套，则由内而外逐层查找，直至最外层的函数)；
    Global - 全局空间(模块enclosed.py)，在模块顶层赋值的filename变量；
    Builtin - 内置模块(__builtin__)中预定义的变量名中查找filename变量；
    在任何一层先找到了符合要求的filename变量，则不再向更外层查找。如果直到Builtin层仍然没有找到符合要求的变量，则抛出NameError异常。这就是变量名解析的：LEGB法则

~~~


#### **55. os和sys模块的作用**
`Python 参考手册`
- 官方文档：
~~~
    os模板提供了一种方便的使用操作系统函数的方法
    sys模板可供访问由解释器使用或维护的变量和与解释器交互的函数
~~~

#### **56. 如何判断是函数还是方法**
- 函数是任何调用方传参进去直接用就好了
- 方法: 必须是某个实例或者类才能调用, 类方法的第一个参数就是类本身, 实例方法第一个参数就是实例本身;

#### **57. 写一个类，并让它尽可能多的支持操作符**
`Fluent Python -- 第13章`

#### **58. Python中如何使用线程池和进程池**
`Python 参考手册`

#### **59. threadlocal的作用**
`廖雪峰 + Python参考手册`
-  Thread Local 对象，就能够让同一个对象在多个线程下做到状态隔离。

#### **60. 简述 asynio模块的作用和应用场景**
`Fluent Python第 18 章 使用 asyncio 包处理并发`
`https://zhuanlan.zhihu.com/p/25228075`
- 根据官方说明， asyncio模块主要包括：
~~~
    1. 具有特定系统实现的事件循环（event loop）;

    2. 数据通讯和协议抽象（类似Twisted中的部分);

    3. TCP，UDP,SSL，子进程管道，延迟调用和其他;

    4. Future类;

    5. yield from的支持;

    6. 同步的支持;

    7. 提供向线程池转移作业的接口;
~~~

#### **61. 33简述 gevent模块的作用和应用场景**
#### **62. twisted框架的使用和应用**
#### **63. range()函数**
- python2：range 数字列表
    xrange 可迭代对象
- python3 ：可迭代对象

#### **64. **


#### **65. 解释一下python的and-or语法**
`Python 参考手册P62`
- and: 逻辑与
- or : 逻辑或
- not: 逻辑非

- 他们都不能重载(Fluent 13.1)

#### **66. hash表是怎么实现的？有冲突的时候怎么处理？**
`数据结构与算法分析P113` -- to be finished
- 内消解:
~~~
    1.  开放地址法: 数据发生冲突时, 就要尝试选择另外的单元, 直到找出空的单元为止;
        a. 线性探测法
        b. 平方探测法
        c. 双散列
~~~
- 外消解:
~~~
    2. 分离链接法

~~~


#### **67. 线程安全是什么意思？新线程什么情况下会影响原有线程？**
`https://zhuanlan.zhihu.com/p/37620890`

#### **68. Python里面match()和search()的区别？**
- re模块中match(pattern,string[,flags]),检查string的开头是否与pattern匹配。re模块中research(pattern,string[,flags]),在string搜索pattern的第一个匹配值

#### **69. 不能被继承的类**

#### **70. tuple和set的区别，set的底层实现**
- set 和 frozenset 的实现也依赖散列表,但在它们的散列表里存放的只有元素的引用(就像在字典里只存放键而没有相应的值)。
~~~
    字典和散列表的几个特点,对集合来说几乎都是适用的:
    a. 集合里的元素必须是可散列的;
    b. 集合很消耗内存;
    c. 可以很高效地判断元素是否存在于某个集合;
~~~

#### **71. __str__ 与 __repr__?**
`Python 参考手册P45`
`Fluent Python 9.1`
- 每门面向对象的语言至少都有一种获取对象的字符串表示形式的标准方式。Python 提供了两种方式:
~~~
    repr()
    以便于开发者理解的方式返回对象的字符串表示形式

    str()
    以便于用户理解的方式返回对象的字符串表示形式;
~~~
- 在打印时, 先调用__str__(), 如果没有定义, 就会调用__repr__()

#### **72. python中的Mixin**
- 自己理解:
~~~
    Mixin是为了给一个类扩充功能用的，它也没法被实例化。我们可以在Mixin类里实现一些方法给类扩充功能，合理使用mixin也能避免复杂的继承关系。你可能会问了，那为啥不直接写在类里头，比如用@staticmethod方法(我就有这个疑问)？我的理解是这样的，为了『高内聚』。如果你用过pylint检测代码，你会发现你在写类的一个方法时，如果在写一个method时没有使用到任何self里的东西，pylint会给提示『R0201 Method could be a function [pylint]』，意思是这个方法可以可以单独写成一个函数，不必要写在类里。也就是说，只有一个类里实现的方法都是使用了self里的数据时才能成为高内聚的（我不知道我这样理解对不对）。例子：flask_login插件有个UserMixin给定义的用户类实现登录功能。关于多重继承和 mixin 在 Ruby 之父的书《松本行弘的程序世界》中有不错的科普。
~~~

#### **73. Python的队列**
`https://zhuanlan.zhihu.com/p/37093602`
- Python标准库中包含了四种队列，分别是
~~~
    queue.Queue / asyncio.Queue / multiprocessing.Queue / collections.deque
~~~

#### **74. Python中的deque是线程安全的吗？**
- 通过查看collections.deque中的append()、pop()等方法的源码可以知道，他们都是原子操作，所以是GIL保护下的线程安全方法(通过dis方法可以看到，append是原子操作（一行字节码）)。

- 首先第一个问题， deque源码里没有用锁保护critical section，是如何实现线程安全的？
~~~
    (1). 看上去没有锁，但实际上是有的，没错就是GIL。
        a. 只有获取了GIL锁的线程才能操作Python对象或调用Python/C API
        b. 什么时候会当前线程会释放GIL呢？一个是python解释器每执行若干条python指令（阈值100）后会尝试做线程切换，让其他线程有机会执行。另一个是进行IO操作时，会释放掉GIL，当前线程进入睡眠
    (2). 那么deque的C语言实现中，以pop为例, 在通过Python/C API调用这个函数时，当前线程肯定是先拿到了GIL的，而在这个函数内部，没有主动释放GIL, 所以整个函数可以看作被GIL保护的critical section
~~~

#### **75. linux 文本文件, 一列姓名, 一列分数, 多行, 如何排序**
- sort -t -k -n -r
~~~
    sort -k 2n test.txt
    以第二行排序
~~~

- Python 实现, 如何能比
~~~
    def sort_by_name():
    with open("test.txt", 'r') as fp:
        rec = []
        content = fp.readlines()
        for c in content:
            remain = c.split()
            rec.append(remain)
        res = sorted(rec, key=lambda x: int(x[-1]))

    with open("test_after_sort", 'w', encoding="utf-8") as fp:
        for r in res:
            s = ''
            for item in r:
                s = s + ' ' + str(item)
            s += '\n'
            fp.write(s)
~~~

#### **76. Python的锁**

#### **77. yield from**
- yield from 是全新的语言结构。它的作用比 yield 多很多,因此人们认为继续使用那个关键字多少会引起误解。在其他语言中,类似的结构使用 await 关键字,这个名称好多了,因为它传达了至关重要的一点:在生成器 gen 中使用 yield from subgen()时,subgen 会获得控制权,把产出的值传给 gen 的调用方,即调用方可以直接控制 subgen。与此同时,gen 会阻塞,等待 subgen 终止。

- yield from x 表达式对 x 对象所做的第一件事是,调用 iter(x),从中获取迭代器。因此,x 可以是任何可迭代的对象;

- yield from 的主要功能是打开双向通道,把最外层的调用方与最内层的子生成器连接起来,这样二者可以直接发送和产出值,还可以直接传入异常

#### **78. concurrent.futures and Asyncio Future**
- concurrent.futures 模块的主要特色是 ThreadPoolExecutor 和ProcessPoolExecutor 类,这两个类实现的接口能分别在不同的线程或进程中执行可调用的对象。这两个类在内部维护着一个工作线程或进程池,以及要执行的任务队列

- a,标准库中有两个名为 Future 的类:concurrent.futures.Future 和 asyncio.Future。这两个类的作用相同:两个 Future 类的实例都表示可能已经完成或者尚未完成的延迟计算。这与 Twisted 引擎中的 Deferred 类、Tornado 框架中的
Future 类,以及多个 JavaScript 库中的 Promise 对象类似。

- 期物封装待完成的操作,并放入队列,完成的状态可以查询,得到结果(或抛出异常)后可以获取结果(或异常)
~~~
    P746  的示例17-4 非常值得一看
    0. .submit() 方法的参数是一个可调用的对象,调用这个方法后会为传入的可调用对象排期,并返回一个期物
    1. concurrent.futures.as_completed, 这个函数的参数是一个期物列表,返回值是一个迭代器,在期物运行结束后产出期物。
    1. 两个 Future 类都有`.add_done_callback()` 方法:这个方法只有一个参数,类型是可调用的对象,期物运行结束后会调用指定的可调用对象;
    2. 这两种期物都有 `.done()` 方法,这个方法不阻塞,返回值是布尔值, 指明期物链接的可调用对象是否已经执行;
    3. `.result()` 方法。在期物运行结束后调用的话,这个方法在两个 Future 类中的作用相同:返回可调用对象的结果,或者重新抛出执行可调用的对象时抛出的异常;
~~~

#### **79. 猴子补丁**
`fluent python 11.3`
- 猴子补丁: 在运行时修改类或模块,而不改动源码。

#### **80. namedtuple**
~~~
Card = collections.namedtuple('Card', ['rank', 'suit'])
~~~

#### **81. 介绍下multiprocessing**
`Python 参考手册P336`

#### **82. Python 日志实践**
`http://python.jobbole.com/81666/`

#### **83. 协程是否是协程安全的**
`https://zhuanlan.zhihu.com/p/40279108`

#### **84. 子内化内置类型**
- 直接子类化内置类型(如 dict、list 或 str)容易出错,因为内置类型的方法通常会忽略用户覆盖的方法。不要子类化内置类型,用户自己定义的类应该继承 collections 模块中的类,例如UserDict、UserList 和 UserString,这些类做了特殊设计,因此易于扩展;

#### **85. Python setdefault的用法**

#### **86.  AVL tree**
`python 数据结构`

#### **87. 红黑树**
`python 数据结构`
`https://blog.csdn.net/xiaxzhou/article/details/74999335`

#### **88. python 垃圾回收**
- python采用的是`引用计数`机制为主，`标记-清除`和`分代收集`两种机制为辅的策略
>1. 引用记数机制
~~~
    Python GC主要使用引用计数（reference counting）来跟踪和回收垃圾。在引用计数的基础上，通过“标记-清除”（mark and sweep）解决容器对象可能产生的循环引用问题，通过“分代回收”（generation collection）以空间换时间的方法提高垃圾回收效率。

    1 引用计数
    PyObject是每个对象必有的内容，其中ob_refcnt就是做为引用计数。当一个对象有新的引用时，它的ob_refcnt就会增加，当引用它的对象被删除，它的ob_refcnt就会减少.引用计数为0时，该对象生命就结束了。

    优点:

    简单
    实时性
    缺点:

    维护引用计数消耗资源
    循环引用
    2 标记-清除机制
    基本思路是先按需分配，等到没有空闲内存的时候从寄存器和程序栈上的引用出发，遍历以对象为节点、以引用为边构成的图，把所有可以访问到的对象打上标记，然后清扫一遍内存空间，把所有没标记的对象释放。

    3 分代技术
    分代回收的整体思想是：将系统中的所有内存块根据其存活时间划分为不同的集合，每个集合就成为一个“代”，垃圾收集频率随着“代”的存活时间的增大而减小，存活时间通常利用经过几次垃圾回收来度量。

    Python默认定义了三代对象集合，索引数越大，对象存活时间越长。

    举例： 当某些内存块M经过了3次垃圾收集的清洗之后还存活时，我们就将内存块M划到一个集合A中去，而新分配的内存都划分到集合B中去。当垃圾收集开始工作时，大多数情况都只对集合B进行垃圾回收，而对集合A进行垃圾回收要隔相当长一段时间后才进行，这就使得垃圾收集机制需要处理的内存少了，效率自然就提高了。在这个过程中，集合B中的某些内存块由于存活时间长而会被转移到集合A中，当然，集合A中实际上也存在一些垃圾，这些垃圾的回收会因为这种分代的机制而被延迟。
~~~

#### **89. Python实现tail -f功能**
`https://zhuanlan.zhihu.com/p/20771481`


#### **90. inspect库的常见用法**
