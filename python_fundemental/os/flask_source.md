# Flask

## Questions
- 请求
- 响应
- 路由
- 上下文
- session

#### **1. 说一下Flask中g是怎么实现的，原理是什么**
- 同问题4

#### **2. Flask蓝图**

#### **3. Flask框架依赖组件**
- Flask是python web框架，主要包含werkzeug和jinja2，前者是一个WSGI工具集，后者用来实现模板处理。

#### **4. flask 上下文**
- 从一个 Flask App 读入配置并启动开始，就进入了 App Context，在其中我们可以访问配置文件、打开资源文件、通过路由规则反向构造 URL。当一个请求进入开始被处理时，就进入了 Request Context，在其中我们可以访问请求携带的信息，比如 HTTP Method、表单域等
- App Context 代表了“应用级别的上下文”，比如配置文件中的数据库连接信息；Request Context 代表了“请求级别的上下文”，比如当前访问的 URL。

- flask 提供两种上下文：application context 和 request context 。app lication context 又演化出来两个变量 current_app 和 g，而 request context 则演化出来 request 和 session。


- 这里的实现用到了两个东西：LocalStack 和 LocalProxy。它们两个的结果就是我们可以动态地获取两个上下文的内容，`在并发程序中每个视图函数都会看到属于自己的上下文`，而不会出现混乱。

- LocalStack 和 LocalProxy 都是 werkzeug 提供的，定义在 local.py 文件中。在分析这两个类之前，我们先介绍这个文件另外一个基础的类 Local。`Local 就是实现了类似 threading.local 的效果——多线程或者多协程情况下全局变量的隔离效果。`

- Local 对象内部的数据都是保存在 __storage__ 属性的，这个属性变量是个嵌套的字典. __ident_func 是 协程的 get_current 或者线程的 get_ident，从而获取当前代码所在线程或者协程的 id。


#### **5. WSGI协议是什么**
- 每个 python web 应用都是一个可调用（callable）的对象。在 flask 中，这个对象就是 app = Flask(__name__) 创建出来的 app, WSGI 协议规定了, Server 和 Application 之间怎么通信;

-WSGI application 非常重要的特点是：它是可以嵌套的。换句话说，我可以写个 application，它做的事情就是调用另外一个 application，然后再返回（类似一个 proxy）。一般来说，嵌套的最后一层是业务应用，中间就是 middleware。这样的好处是，可以解耦业务逻辑和其他功能，比如限流、认证、序列化等都实现成不同的中间层，不同的中间层和业务逻辑是不相关的，可以独立维护；而且用户也可以动态地组合不同的中间层来满足不同的需求。

#### **5. flask源码中都有end_point， end_point有什么用**
- 端点通常用作反向查询URL地址（viewfunction**–>endpoint–>**URL）。例如，在flask中有个视图，你想把它关联到另一个视图上（或从站点的一处连接到另一处）。不用去千辛万苦的写它对应的URL地址，直接使用URL_for()就可以了


#### **6. flask路由规则**
- 流程：
~~~
    flask 的路由过程大致的流程：
        1. 通过 @app.route 或者 app.add_url_rule 注册应用 url 对应的处理函数
        2. 每次请求过来的时候，会事先调用路由匹配的逻辑，把路由结果保存起来
        3. dispatch_request 根据保存的路由结果，调用对应的视图函数
~~~

- werkzeug 最核心的路由功能：添加路由规则

#### **7. Werkzeug(Flask)之Local、LocalStack和LocalProxy**
`https://www.jianshu.com/p/3f38b777a621`

#### **8. 为什么实用LocalStack对Local对象进行操作?**

#### **9. Flask中多app应用是怎么完成**
#### **10. Flask框架默认session处理机制**

#### **11. Flask框架中的Local对象和threading.local对象的区别**
- Werkzeug 没有直接使用 threading.local，而是自己实现了 werkzeug.local.Local 类。后者和前者有一些区别：
~~~
    1. 后者会在 Greenlet 可用的情况下优先使用 Greenlet 的 ID 而不是线程 ID 以支持 Gevent 或 Eventlet 的调度，前者只支持多线程调度；
    2. WSGI应用也无法保证每个http请求使用的都是不同的线程，因为后一个http请求可能使用的是之前的http请求的线程，这样的话存储于thread local中的数据可能是之前残留的数据, 后者实现了 Werkzeug 定义的协议方法 __release_local__，可以被 Werkzeug 自己的 release_pool 函数释放（析构）掉当前线程下的状态，前者没有这个能力 
~~~
#### **12. 简述Tornado框架的特点**
#### **13. 简述Tornado框架中Future对象的作用**
#### **14. Tornado操作MySQL使用的模块**
#### **15. Tornado操作redis使用的模块**
#### **16. 简述Tornado框架的适用场景**
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **
#### **. **