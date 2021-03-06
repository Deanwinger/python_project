# Design Data_intensive Application
`Design Data Intensive Application`

### **第一章. 可靠性， 可扩展性，可维护性**
- 可靠性
    - pass

- 可扩展性
    - 描述负载： Twitter的例子(非常值得一读)

- 可维护性
    - pass

================================================================================================================================================================================================

###  **第二章. 数据模型和查询语言**
`TO BE FINISHED`
> summary： 讨论了数据模型和查询语言， 即程序员将数据录入数据库的格式，以及再次要回数据的机制；

================================================================================================================================================================================================

### **第三章. 存储与检索**
> summary: 数据库如何存储我们提供的数据，以及如何在我们需要时重新找回数据；为了高效查找数据库中的特定的键的值，我们需要一个数据结构： 索引，本章将介绍一系列的索引结构，索引背后的大致思想是， 保存一些额外的元数据作为看路标， 帮助你找到想要的数据；索引是主数据衍生的附加结构， 而维护额外的结构会产生开销（每次写入和更新都要更新索引）；

- 哈希索引
~~~
    1. 实施中需要考虑的东西：
        a.文件格式
        b.删除记录
        c.崩溃恢复
        d.部分写入记录
        e.并发控制
    2. 局限：
        a. 散列表必须能放进内存；
        b. 范围查询效率不高；
~~~

- SSTables(Sorted String Table)
`TO BE FINISHED`
~~~
    1.
    2.
~~~

- B树
~~~
    1. 为防止数据库崩溃损失，B树通常会带一个额外的磁盘数据结构，预写式日志（write-ahead-log, 也称为redo log）， 这是一个仅追加的文件，当数据库在崩溃后恢复时，用来使B树恢复到一致的状态；
    2. B树的优化；
~~~

- 比较B树和LSM树
    - LSM树的优点
    ~~~
    1. B树索引必须两次写入每一段数据， 一次预先写入日志，一次写入树页面本身；
    2. LSM树通常比B树支持更高的写入吞吐量；
    3. LSM树可以被压缩的更好，比B树在磁盘上产生更小的文件；
    ~~~
    - LSM树的缺点
    ~~~
    1. 压缩过程可能干扰到正在运行的读写操作；
    2. 磁盘的有限写入带宽，需要在初始写入（记录和刷新内存表）和在后台运行的压缩线程之间共享；
    ~~~

#### **第四章.编码与演化**
- pass

================================================================================================================================================================================================

#### **第五章.复制**
- 1. 主从复制（领导者与追随者）
    - 定义
    ~~~
        (1). 副本之一的被指定为领导者--主库，当客户端需要向数据库写入时，它必须要将请求发送给领导者，领导者将这些数据写入其本地存储；
        (2). 其他副本被称为追随者--从库，当主库写入本地数据时，它会将数据变更发送给所有的追随者，称之为复制日志，每个跟随者从领导者拉取日志，并相应更新其本地数据库；
        (3). 当客户端想要读取数据时，可向主库或者是从库查询，但只有领导者才能接受写操作（从客户端的角度来看， 从库都只是可读的）；
    ~~~
    - 方法：
        - 同步
        ~~~
            - 同步优点
                (1). 从库保证有与主库一致的最新数据；
            - 同步缺点
                (1). 如果同步从库没有响应，主库就无法完成写入操作；
            - 拓展：半同步
                (1). 在数据库上启动启用同步复制，通常意味着其中一个追随者是同步的，而其他的则是异步的，如果同步从库变得不可用或者是缓慢，则使一个异步从库同步，这保证你至少在两个节点拥有最新的数据副本；
        ~~~
        - 异步： 通常情况下，基于领导者的复制，都配置为完全异步；
        ~~~
            - 异步优点
                (1). 即使所有的从库都落后了，主库也可以继续处理写入；
            - 异步缺点
                (1). 如果主库失效且不可恢复，则任何尚未复制给从库的写入都会丢失；
        ~~~

    - 实践：
        - 设置新从库
        ~~~
            (1).在某个时刻获取主库的一致性快照；
            (2).将快照复制到新的从库节点；
            (3).从库连接主库，并拉取快照之后发生的所有数据变更， 这要求快照与主库复制日志中的位置精确关联， 该位置有不同的名称，mysql将其称为二进制日志坐标；
        ~~~
        - 从库失效： 追赶恢复
        ~~~
            (1).从库可以从日志中知道，在发生故障之前处理的最后一个事务，因此，从库可以连接到主库，并请求这之后的所有数据变更；
        ~~~
        - 主库失效： 
            - 故障转移：其中一个从库需要被提升为新的主库，需要重新配置客户端，以将他们的写操作发送给新的主库，其他从库需要开始拉取来自新主库的数据变更；
            - 基本步骤:
            ~~~
                (1). 确认主库失效,如果一个节点再一段时间内没有响应,就认为它挂了;
                (2). 选择一个新的主库, 选择一个新的主库, 最佳人选通常是拥有旧主库最新数据副本的从库,让所有的节点同意一个新的领导者,这是一个共识问题;
                (3).重新配置系统以启用新的主库,如果老的领导者回来, 系统需要确保老领导认可新领导,成为一个从库;
            ~~~
            - 主要麻烦(分布式系统的主要麻烦)
            ~~~
                (1). 如果使用异步复制, 则新主库可能没有没收老主库宕机前的最后一些写入, 如果老主库后续重新加入集群,可能会与新主库的写入出现冲突, 最常见的解决方法是简单的丢弃老主库未复制的写入;
                (2). 如果数据库需要和外部存储相协调,那么丢弃写入内容是极其危险的操作(github的案例);
                (3). 脑裂(两个节点都以为自己是主库)的存在, 非常危险: 如果两个主库都可以接手写操作, 却没有冲突解决机制,数据就有可能丢失或者是损坏;
                (4). 主库被宣告死亡之前,正确的超时应该怎么配置?
            ~~~
    - 原理:
        - 基于主库的复制方式
        ~~~
            (1).基于语句的复制: 主库记录下它执行的每一个写入请求, 并将该语句发送给其从库
                - 缺点:
                    a. 任何调用非确定性函数的语句, 可能生成不同的值;
                    b. 如果语句出现了自增列, 或者依赖数据库中的现有数据, 则必须在每个副本上按照完全相同的顺序执行它们;
                    c. 有副作用的语句(触发器,存储过程, 用户自定义的函数), 可能会在每个副本产生不同的副作用;

            (2).传输预写式日志(WAL)
            (3).从库连接主库，并拉取快照之后发生的所有数据变更， 这要求快照与主库复制日志中的位置精确关联， 该位置有不同的名称，mysql将其称为二进制日志坐标；
        ~~~

================================================================================================================================================================================================

#### **第六章.分区**
- 目标: 将数据和查询的负载均匀分布在各个节点上, 如果每个节点公平分享数据和负载,那么理论上10个节点应该能够处理10倍的数据量和10倍单个节点能够处理的读写吞吐量;

- 热点:如果分区是不公平的,一些分区比其他分区有更多的数据或查询, 我们称之为偏斜(skew)--极端情况,有可能所有的负载全部落在一个节点上,不均衡导致的高负载分区被称为热点;
~~~
    解决办法:
    1. 将记录随机分配给节点,
        缺点: 当读取时无法知道再哪个节点上,所以必须并行的查询所有的节点;

    2.根据键的范围分区:
        优点: 进行范围扫描非常的简单;
        缺点: 某些特定的访问模式会导致热点(例如主键是时间戳,如果每天分配一个分区);

    3.使用散列函数来确定键的分区
        具体实践: 一旦选择了一个合适的键散列函数, 可以为每个分区分配一个散列范围,分区边界可以是均匀分布的,也可以是伪随机选择的(这种情况下,该技术也被称为一致性哈希)
        一致性哈希: 是一种能均匀分配负载的办法, 他使用随机选择的分区边界来避免中央控制或分布式一致性的需要;
        缺点: 失去了高效执行范围查询的能力;
~~~

- 负载倾斜与热点消除
    - 哈希分区可以帮助减少热点;但是不能完全避免(如某个流量巨星的新闻--微博热点);
    ~~~
    举例(同时参考第一章--描述负载):
        社交媒体上一个拥有数百万追随者的名人用户再做某事时可能会导致大量的写入同一个键;
    解决办法:
        如果一个主键被认为是非常火爆的, 一个简单的方法是在主键的开始或结尾添加一个随机数, 从而存储在不同的分区, 不过之后的读取都需要做额外的工作,读取与合并,同时还需要额外的记录, 只需要对少量热点附加随机数, 需要跟踪哪些键是要被记录跟踪的;
    ~~~

================================================================================================================================================================================================

#### **第七章.事务**
- 1. ACID
    - 定义:
    - 单对象 与 多对象操作
    ~~~
        a. 例子7.2， 违反隔离性要求--一个事务读取另一个事务未被执行的写入(脏读)
        b. 例子7.3， 对原子性的需求
        c. 单对象写入: 
            - 对单节点的单个对象上提供原子性和隔离性；原子性可以通过使用日志来实现崩溃恢复，隔离性可以通过在每个对象上使用锁来实现；
        d.事务通常被理解为：将多个对象上的多个操作合并为一个执行单元的机制；
    ~~~

- > 2. 弱隔离级别（nonserializable）
    - (1) read uncommitted (读未提交)
    ~~~
        a.可以防止脏写， 但是不能防止脏读；
    ~~~
    - (2) read committed (读已提交)
    ~~~
        - part I fundemental：
            a.从数据库读的时候，只能看到已提交的数据（没有脏读）：
                - 脏读：如果一个事务已经将一些数据库写入数据，但是事务还没有正式的提交或者是终止，另一个事务能看到未提交的数据吗？如果是的话，那就叫做脏读；
                - 没有脏读， 意味着事务的任何写入操作只有在该事务提交时才能被其他人看到；
                - 防止脏读的原因：
                    - 如果事务要更新多个多想，脏读意味着另一个事务可能只看到一部分的更新， 可能导致其他事务作出错误的决定；
                    - 如果事务中止，则所有的数据需要回滚，脏读导致看到错误的数据；

            b.写入数据库的时候，只会覆盖已经写入的数据（没有脏写）：
                - 脏写： 如果两个事务同时尝试更新数据库中的对象， 会发生什么情况，我们不知道写入的顺序是怎样的，但是我们通常认为后面的写入会覆盖前面的写入， 如果先前的写入是尚未提交事务的一部分，后面的写入会覆盖一个尚未提交的值，这样被称为脏写；
                - 通常是延迟第二次写入，直到第一次写入事务提交或者是中止为止；
                - 通过防止脏写，这个隔离级别避免了一些并发问题：
                    - 图7.5的例子（脏写导致不好的例子），车子卖给了Bob， 但是账单寄给了Alice，这就是部分更新的问题
                    - 无法解决图7.1带来的计量器增量安全的问题（防止更新丢失中将讨论如何解决）
                    
        - part II 实现读已提交
            a. 数据库通过使用行锁来防止脏写：当事务想要修改特定的对象（行或者文档）时，他必须首先获得该对象的锁；
            b. 如何防止脏读
                - 方法一：使用相同的锁（行锁），要求任何要读取对象的事务先获取该锁，然后在读取之后释放该锁；缺点： 如果有大量的写业务的时候，将导致读事务大量的排队；
                - 方法二（通常的方法）：对于写入的每个对象，数据库都会记住旧的已提交的值，和当前持有写入锁的事务持有的新值， 当事务正在进行时，任何其他读取对象的事务都会拿到旧值， 只有当新事务提交时，才会切换到读取新值；
            c.
            d.
    ~~~
    - (3) 可重复读（repeatable read）
    ~~~
        - part I fundemental：
            a. 读已提交可能出现的问题--读偏差（又叫不可重复读）的例子：
                - 银行账号余额的问题（图7.6）
                - 大部分情况下可以接受，但是有些情况下不能接受：
                    - 备份
                    - 分析查询和完整性检查
            b. 快照隔离是这个问题最常见的解决方法；

        - part II 实现快照隔离：
            a. 原理：每个事务都可以从数据库的一致性快照中读取--也就是说，事务可以看到事务开始时在数据库中提交的所有数据，即使这些数据随后被另一个事务更改，每个事务也只能看到该特定时间点的旧数据；
            b. 与读已提交类似，快照隔离的实现通常用写锁来防止脏写；
            c. 关键原则：读不阻塞写，写不阻塞读；
            d. 支持快照隔离的引擎通常也使用MVCC来实现读已提交隔离级别；
            e. 具体实现技术： 多版本并发控制（MVCC）
                - 为了实现快照隔离，数据库必须保留一个对象的几个不同的提交版本，因为正在进行的事务可能需要看到数据库在不同的时间点的状态，因为它并排的维护着多个版本的对象，所有又被称为：多版本并发控制；
                - 以PostgreSQL为例：
                    - 当一个事务开始时， 它被赋予一个唯一的， 永远增长的事务ID，每当事务写入内容的时候，它所写入的数据都会被标记上写入者的事务ID；
            f.一致性快照的可见性规则：
                - 每当事务开始时，数据库列出当时所有其他（尚未提交或者中止的）的事务清单，即使后面提交了，这些事务的写入也会被忽略；
                - 被中止事务所执行的任何写入都将被忽略；
                - 由具有较晚事务ID的事务的所有的写入都将被忽略， 不管这些事务是否已经提交；
                - 所有其他写入，对应用都是可见的；

    ~~~
    - (4) 防止丢失更新：
        - 前提：目前已经讨论的读已提交和快照隔离级别，主要保证了只读事务在并发写入时可以看到什么，却忽略了两个事务并发写入的问题--我们只讨论了脏写，一种特定类型的写写冲突是可能出现的（最著名的是丢失更新lost update）--两个并发计数器增量为例；

        - 解决方案：
            - 1. 原子写：许多数据库提供原子更新操作，如果你的代码可以通过这些操作来表达，那这通常是最好的解决方案；
                - 原子操作通常通过在读取对象时，获取其上的排他锁来实现，以便更新完成之前没有其他事务可以读取它，这种技术又被称为游标稳定性；
                - 另一种选择是简单地强制所有的原子操作在单一线程上执行；
            - 2. 显式锁定：
                - 如果数据库本身没有提供必要的功能，可以让应用程序显式的锁定将要更新的状态（应用程序可以执行读取-修改-写入序列， 如果任何其他事务尝试同时读取同一对象， 则强制等待， 直到第一个读取-修改-写入序列完成）；
            - 3. 自动检测丢失更新：
                - 原子操作和锁是通过强制读取-修改-写入序列按顺序发生，来防止丢失更新的方法， 另一种方法是允许他们并行执行， 如果事务管理器检测到丢失更新，则中止事务并强制他们重试其读取-修改-写入序列；
            - 4. 比较并设置CAS （compare and set）
                - 只有当前值从上一次读取时一直未改变，才允许更新发生， 如果当前值与先前读取的值不匹配，则更新不起作用；
            - 5. 冲突解决和复制：在复制数据库中，防止丢失的更新需要考虑到另一个纬度：由于在多个节点上存在数据副本，并且不同节点的数据可能被并发的修改，因此需要一些额外的步骤来防止丢失更新；`此节存疑--To Be Finished`

    - (5) 写入偏差和幻读：
        - summary：可以将写入偏差视为丢失更新问题的一般化，如果两个事务读取相同的对象，然后更新其中的一些对象（不同的事务可能更新不同的对象），则可能发生写入偏差；在多个事务更新同一个对象的特殊情况，就有可能发生脏写或丢失更新；
        - 之前那些方法对于不同对象受限：
            - 由于涉及多个对象， 单对象的原子操作不起作用；
            - 自动检测丢失更新无效， 自动防止写入偏差需要真正的可序列化隔离；
            - 某些数据库允许配置约束，然后由数据库强制执行（例如唯一性限制）；
            - 如果无法使用可序列化的隔离级别，次优选项是显示锁定事务所依赖的行；
        - 写入偏差的更多例子：
            - `值得一看` 
        - 导致写入偏差的幻读（上述的例子都遵循相同的模式， 结合例子来体会相同的模式）：
            - 幻读： 一个事务中的写入改变另一个事务中的搜索查询的结果；（结合写偏差的几个例子来研究， 更便于理解）
                - 事务从数据库读取一些数据，检查查询的结果，并根据看到的结果决定采取一些操作，但是在快照隔离的情况下，原始查询的结果在事务的提交时可能已经不是最新的了，因为数据可能在同一时间被修改；
                - 通用模式：
                ~~~
                    a. 一个select查找出符合条件的行，并检查是否符合一些要求；
                    b. 按照第一个查询结果，应用代码决定是否继续；
                    c. 如果应用决定继续操作，就执行写入，并提交事务；
                ~~~
                - 数据库如何知道查询结果是否已经变了呢？
                ~~~
                    a. 检测对旧MVCC对象版本的读取（读之前存在未提交的写入）；
                    b. 检测影响先前读取的写入（读之后发生写入）；
                ~~~

- > 3. 可序列化
    - 前提精要：读已提交和快照隔离级别会阻止某些竞争条件，但不会阻止另一些，比如写入偏差和幻读， 具有可序列化隔离级别的数据库必须防止幻读；
    - 定义：可序列化隔离通常被认为是最强的隔离级别，它保证事务即使是并行执行的， 最终的结果也是一样的， 就好像他们没有任何并发性，连续挨个执行的；
    - 目前提供可序列化的数据库使用了以下三种技术之一：
        - 字面意义上的串行顺序执行事务；
        - 2PL（two-phase locking）， 几十年的来唯一可行的选择；
        - 乐观并发控制技术
    - （1）. 真的串行执行
        - 在存储过程中封装事务：存储过程和内容存储，使得在当个线程上执行所有的事务变得可行；
        - 串行执行的小结： `可以一样，意义不大`
    
    - （2). 两阶段锁定（2PL）
        - 大约30年来，在数据库中只有一种广泛使用的序列化算法：两阶段锁定；
        - 只要没有写入，就允许多个事务同时读取同一个对象，但对象只要有写入，就需要独占访问权限：
        ~~~
            a. 如果事务A 读取了一个对象，并且事务B想要写入该对象，那么B必须等到A提交或中止才能继续；
            b. 如果事务A 写入了一个对象，并且事务B想要读取该对象，那么B必须等到A提交或中止才能继续；
        ~~~
        - summary：在2PL中，写入不仅会阻塞其他的写入，也会阻塞读，快照隔离使得读不阻塞写，写不阻塞读，这是2PL和快照隔离的关键区别，另一方面，2PL可以防止早先讨论的所有竞争条件， 包括丢失更新和写入偏差；
        - 实现两阶段锁
        ~~~
            a.读和写的阻塞是通过为数据库中每个对象添加锁来实现的，锁可以处于共享模式或独占模式，锁使用如下：
                - 若事务要读取对象，则需先以共享模式获取， 允许多个事务同时持有共享锁，但如果另一个事务已经在对象上持有排他锁， 则这些事务必须等待；
                - 若事务要写入对象，那他必须首先以独占模式获取该锁，如果对象上已经存在任何的锁了，该事务就必须等待；
                - 如果事务先读取再写入对象，则他可能会将其共享锁升级为独占锁，升级锁的工作和直接获取排他锁相同；
            b. 可能会出现死锁，数据库会自动检测事务之间的死锁，并中止其中一个，以便另一个继续执行， 被中止的事务需要由应用程序重试；
        ~~~
        - 两阶段锁定的性能
        ~~~
            a. 获取和释放锁；
            b. 并发性的降低，如果两个并发事务试图做任何可能导致竞争的事，那么必须等待另一个完成；
            c. 可能发生的死锁；
        ~~~
        - 谓词锁 与 索引范围锁（间隙锁）以及可序列化快照隔离
        `可以作为拓展阅读`
        ~~~
            - 谓词锁的性能不佳，如果活跃的事务有很多锁，检查匹配的锁会非常的耗时，因此，大多数使用2PL的数据库实际上实现了索引范围锁，这是一个简化的近似版谓词锁；
        ~~~

    - （3）summary: **`悲观与乐观的并发控制`**
        - 两阶段锁是一种所谓的悲观并发控制机制：如果有事情可能出错，最好等到情况安全之后再做任何事；
            - 串行执行可以被称为悲观到了极致：在事务持续期间，每个事务对整个数据库居于排他锁；
        - 序列化快照隔离是一种乐观的并发控制技术：如果存在潜在的危险，也不阻止事务，当一个事务想要提交时，数据库检查是否有什么不好的事发生（即隔离是否被违反），如果是的化， 事务将被中止， 并且必须要被重试，只有可序列化的事务才被允许提交；

        
- 4. 
================================================================================================================================================================================================
#### **第八章.事务**


================================================================================================================================================================================================
#### **第九章.事务**

================================================================================================================================================================================================
#### **第十章.事务**
