# Redis
`redis设计与实现`
`redis开发与运维`

## Part I fundemental
~~~
    查看redis相关进程
    ps -ef | grep redis
~~~


#### **1. 单进程**
- 对读写事件的响应是通过对epoll函数的包装来做到的;
- select 命令切换数据库;
- DBsize 查看当前数据库的key的数量;
- Flushdb: 清空当前库;
- Flushall: 通杀全部库;
- redis索引都是从0 开始;
- 默认端口6379;

#### **2. 五大数据类型**
- string
- Hash: 键值对集合, string类型为键和value的映射表;
- List: 底层是链表, 所以前后都可以插入;
- Set: string 类型的无序无重复集合, 底层通过hash实现;
- Zset: (有序无重复的集合): 每个元素都会关联一个double类型的分数; redis通过分数从小到大进行排序; 成员是唯一的, 但是分数却可以重复;

#### **3. 常见key(键)操作**
- key * 获取所有的键列表;
- exists key 判断key 是否存在;
- move key db --> 当前库就没有了, 被移到db了;
- expire key second -- > 给key设置过期时间;
- ttl(time to live) key --> 查看还有多少秒过期(-1 表示永不过期, -2表示已经过期, 终结就会移除出数据库)
- type key --> 查看key是什么类型;

#### **4. 常见string操作**
- set/get/del/append/strlen key;
- Incr/decr key; 一定要数字才能进行加减, 默认是1; /incrby/decrby key m(数字);
- getrange/setrange key m n; m和n为index;(范围内取值, 范围内设值)
- setex(set with expire)键秒值/setnx(set if not exist)
~~~
    setex k1 10 v1;
~~~
- mset/mget/msetnx 一次性设多值;
~~~
    mset k1 v1 k2 v2 k2 v3;
~~~

#### **5. 常见list操作**
`单值多value`
- lpush/rpush/lrange
~~~
    lpush list0 1 2 3 4 5
    lrange list0 0 -1
~~~
- lpop/rpop
- lindex: 按照索引下标获得元素
~~~
    lindex list0 3
~~~
- llen: len()函数
- lrem (n) key 删除n个value
~~~
    lrem list0 2 3 (原112233, 删后变1122)
~~~
- ltrim key start end
~~~
     截取index 从start 到 end 范围内的元素, 并把截取的值重新赋值给key
~~~
- rpoplpush source dest

- lset key index value

- linsert key before/after value
~~~
    linsert list0 before x y -- 将y插入x前
~~~
- 总结
~~~
    1. 字符串链表, left, right 都可以插入添加;
    2. 如果键不存在, 创建新的链表;
    3. 如果值全部移除, 键相应的也消失;
    4. 头尾操作效率高;
~~~

#### **6. 常见set操作**
`单值多value`
- sadd/smembers/sismember
~~~
    sadd set0 112233
    smember set0
    sismember set0 x
~~~

- scard key -- 获取集合里的元素个数;
~~~
    scard set0 
~~~
- srem key value
~~~
    srem set0 x
~~~
- srandmember key n(某个整数) -- 随机出n个值;
- spop key --随机出栈;
- smove key1 key2
~~~
    smove set0 set1 5 -- 将set0中的5移入set1
~~~

- sdiff key1 key2 
~~~
    sdiff set01 set02 -- 在set01里, 不在set02里的项;
~~~

- sinter 交集
~~~
    sinter set01 set02;
~~~
- sunion 并集


#### **5. 常见hash操作**
`kv模式不变, 但v是一个键值对`
- hset/hget/hmset/hmget/hgetall/hdel
~~~
    hset user id 11, key是user, value是 id 11
    hmset customer id 11 name li4 age 26
    hmget customer id name age
    hgetall customer
    hdel customer name
    hlen customer
    hexists customer id 判断是否存在值

~~~

- hkeys/hvals
~~~
    hkeys customer 获取customer 对应的对象的所有的keys
~~~

- hincrby/hincrbyfloat
~~~
    hincrby customer age 2
~~~

- hsetnx
~~~
    hsetnx customer email xxx@aaa.com
~~~

#### **6. 常见Zset操作**
`再set 的基础上, 加一个score值`
- zadd/zrange
~~~
    zadd zset0 60 v1 70 v2 80 v3
    zrange zset0 0 -1
    zrange zset0 0 -1 (withscore) 才会显示全部, 否则只显示各个value值
~~~


- zrangebyscore key
~~~
   zrangebyscore zset0 60 90
   zrangebyscore zset0 60 (90  指代不包含
~~~

- zrem key
~~~
    zrem zset01 v5    
~~~

- zcard/zcount key score 
~~~
    zcard zset0 --统计对应的value的个数, 不包括score
    zcount zset0 60 80 -- 统计范围内score个数
~~~

- zrank key values/ zscore key
~~~
    zrank zset0 v3 -- 拿到下标, index
    zscore zset0 v3 -- 拿到分数 
~~~

- zrevrank key values -- 获取逆序下标
~~~
    zrevrank
~~~

- zrevrange key 
~~~
    zrevrange zset0 0 -1
~~~

- zrevrangebyscore zset 80 60 -- 逆序获取范围

#### **7. redis 的持久化**
- RDB

- AOF

#### **8. 介绍下RDB指令**
- save: 在指定的时间间隔内, 将内存中的数据集快照写入磁盘;
~~~
    1. redis会单独创建一个子进程来进行持久化, 会先将数据写入到一个临时文件, 待持久化过程结束, 再用当前这个临时文件来替换上次持久化的文件;
    2. 整个过程中, 主进程是不进行任何IO操作的, 确保了性能;
    3. 如果需要大规模的数据恢复, 且对数据完整性不是非常敏感, 那RDB方式要比AOF方式更加高效;
    4. RDB的缺点就是最后一次持久化的数据可能丢失;
    5. 保存dump.rdb文件;
    6. 快照触发条件:
        1分钟 1万次
        5分钟 10次
        15分钟 1次

        禁用 rdb
        save ""

        save -->马上备份
~~~

- stop-writes-on-bgsave-error
~~~
    后台保存数据出错, 前台停止写入
~~~

- rdbcompression: 对于存储到磁盘中的快照, 是否进行压缩存储; 默认是yes

- rdbchecksum: 存储快照后, 是否使用crc64算法进行数据校验, 这样会增加大约10%的性能损耗; 默认是yes

#### **9. 如何触发RDB快照**
- save: 只管保存, 其他不管, 全部阻塞;
- bgsave: 后台异步进行快照操作, 同时可以相应客户端请求; 
- lastsave: 最后一次成功执行快照的时间;
- 执行flushall命令, 也会产生dump.rdb文件, 但是里面是空的;

#### **10. RDB如何恢复**
- 将备份文件dump.rdb移动到redis安装目录并启动服务即可;

#### **11. RDB优势和劣势**
- 优势
~~~
    1. 适合大规模的数据恢复;
    2. 如果对数据完整性和一致性要求不高, 对比AOF更有优势;
~~~
- 劣势
~~~
    1. 最后一次修改可能会丢失
    2. fork操作
~~~

#### **12. 介绍下AOF指令**
- 以日志的形式来记录每个写操作, 只追加, 不改写,故障重启的话, 就根据日志文件重写指令; 默认为不开启;
- 如果aof文件出问题, redis-check-aof --fix appendonly.aof
- appendfsync:
~~~
    1. always: 同步持久化, 每次发生数据变更,都会立即记录到磁盘;
    2. everysec: 出厂默认, 异步操作, 每秒记录, 如果一秒内宕机, 有数据丢失;
    3. no: 关闭;
~~~

- aof启动/修复/恢复
~~~
    1. 启动: 修改默认的appendonly no为 yes
    2. 修复: redis-check-aof
    3. 恢复: 重启redis然后重新加载
~~~

- rewrite
~~~
    1. 是什么:
        AOF 采用文件追加方式, 文件大小超过阙值时, redis会启动AOF文件的内容压缩, 只保留可以恢复数据的最小指令集,命令 bgrewriteaof
    2. 重写原理
        AOF文件持续增长而过大时, 会fork出一条新进程来将文件重写, 
    3. 触发机制
        redis会记录上次重写时的AOF大小, 默认配置是上次rewrite后的大小的一倍, 且问价大小大于64M;
    
    no-appendfsync-on-rewrite: 重写时是否运用appendfsync, 用默认的no即可, 保证数据的安全性;
    auto-aof-rewrite-min-size 设置重写的基准值
    auto-aof-rewrite-percentage 设置重写的基准倍数
~~~

- 优势
~~~
    1. 可以是每秒同步, 每修改同步, 不同步;
~~~

- 劣势
~~~
    1. aof文件远大于rdb, 恢复速度较慢;
    2. aof运行效率要慢于rdb, 每秒同步效率较好;
~~~

- 总结:
~~~
    官网建议:
    1. rdb可以在指定的时间间隔对你的数据进行快照存储;
    2. aof, 写文件, 重读一遍;
    3. 只做缓存;
    4. 同时开启两种持久化方式; -- 服务器重启时, 会优先找aof文件;
~~~

- 性能建议:
~~~
    1. 因为rdb文件只用作后备用图, 建议只在slave上持久化RDB, 保留save 900 1这条规则;
    2. 如果开启aof, 好处是, 最恶劣的情况下, 也只会丢失不超过两秒的数据, 代价是带来了持续的IO, 再是aof rewrite过程中产生的新数据写到新文件造成的阻塞是不可避免的,只要硬盘允许, 应该尽量减少AOF rewrite的频率, 默认64M太小, 建议改到5G; 
    3. 如果不开启 aof, 也可以仅靠master-slave republication, 能省掉一大笔IO的同时, 也减少了rewrite带来的系统波动, 代价是, 如果master/slave同时倒掉, 会丢失十几分钟的数据;
~~~

#### **13. 事务**
- case1:  正常执行
~~~
    1. 开启事务: MULTI 
    2. 执行: EXEC
    3. 放弃操作: DISCARD
~~~

- case2: 全体连坐: 事务的原子性

- case3: 冤头债主
~~~
    case2, 3 有一些tricky, 
        case2的连坐是指在解析语法时, 不能出错(比如 错误的命令 getset v1),;
        case3的情况是解析完成之后, 执行时如果出错, 这条不执行, 其他正常完成, 比如 incr k1(对应的字符串), 后续没有问题, 则只有这条无效;

        正因为这个原因, redis对事务的支持是部分支持;
~~~

- watch 监控 
~~~
    watch 指令类似乐观锁, DDIA 第七章CAS有讲;

    1. 悲观锁
    2. 乐观锁
    3. CAS(check and set)
~~~
- unwatch

- 总结:
~~~
    1. 单独的隔离操作, 事务中所有的命令都会序列化, 按顺序地执行;
    2. 不保证原子性;
~~~

#### **14. 消息订阅, 发布**
- 定义:
~~~
    1. 进程间的一种通信通信模式: 发送者(pub)发送消息, 订阅者(sub)订阅消息;
~~~
- SUBSCRIBE -- 订阅频道(多个)
~~~
    SUBSCRIBE new1 news2 news3
~~~

- publish -- 发布
~~~
    publish new1 hello-world
~~~

- psubscribe 通配符订阅多个
~~~
    psubscribe new*
~~~

#### **15. 主从复制**
- master/slave 机制
~~~
    1. 主机数据更新后, 自动更新到备机的机制;
    2. master 以写为主, slave 以读为主;
~~~

- 如何操作:
~~~
    1. 配从库不配主库;
        指令: slaveof 主库IP 主库端口;
        注意事项:
            a.每次与master断开之后, 都需要重新连接, 除非你配置进redis.conf;

    第一步:
        info republication
~~~



## Part II Question

- redis, kafka, rabbitMQ, celery

#### **1. redis LRU策略**
`http://blog.jobbole.com/107084/`
`印象笔记`


#### **2. Redis与Memorycache的区别？**
- 优势
(1) memcached所有的值均是简单的字符串，redis作为其替代者，支持更为丰富的数据类型

(2) redis的速度比memcached快很多

(3) redis可以持久化其数据

#### **3. 渐进式rehash过程**
#### **4. 持久化机制**
#### **5. redis的aof太大如何优化**
#### **6. 启动过程**
#### **7. 集群， redis集群，如何拓展**
~~~
    1twemproxy。大概概念是，它类似于一个代理方式，使用方法和普通redis无任何区别，设置好它下属的多个redis实例后，使用时在本需要连接redis的地方改为连接twemproxy，它会以一个代理的身份接收请求并使用一致性hash算法，将请求转接到具体redis，将结果再返回twemproxy。使用方式简便(相对redis只需修改连接端口)，对旧项目扩展的首选。 问题：twemproxy自身单端口实例的压力，使用一致性hash后，对redis节点数量改变时候的计算值的改变，数据无法自动移动到新的节点。

    2.codis: 目前用的最多的集群方案，基本和twemproxy一致的效果，但它支持在 节点数量改变情况下，旧节点数据可恢复到新hash节点。

    3.redis cluster3.0自带的集群，特点在于他的分布式算法不是一致性hash，而是hash槽的概念，以及自身支持节点设置从节点。具体看官方文档介绍。

    4.在业务代码层实现，起几个毫无关联的redis实例，在代码层，对key 进行hash计算，然后去对应的redis实例操作数据。 这种方式对hash层代码要求比较高，考虑部分包括，节点失效后的替代算法方案，数据震荡后的自动脚本恢复，实例的监控，等等。
~~~

#### **8. Redis的6种数据淘汰策略**
~~~
    1. noeviction:返回错误当内存限制达到并且客户端尝试执行会让更多内存被使用的命令（大部分的写入指令，但DEL和几个例外）

    2. allkeys-lru: 尝试回收最少使用的键（LRU），使得新添加的数据有空间存放。

    3. volatile-lru: 尝试回收最少使用的键（LRU），但仅限于在过期集合的键,使得新添加的数据有空间存放。

    4. allkeys-random: 回收随机的键使得新添加的数据有空间存放。

    5. volatile-random: 回收随机的键使得新添加的数据有空间存放，但仅限于在过期集合的键。

    6. volatile-ttl: 回收在过期集合的键，并且优先回收存活时间（TTL）较短的键,使得新添加的数据有空间存放。
~~~

#### **9. redis的并发竞争问题**
#### **10. 如何将数据分布在不同的Redis**
#### **11. 谈谈redis的事务**
#### **12. 什么是Redis？简述它的优缺点？**
>1. Remote Dictionary Server
~~~
    Redis本质上是一个Key-Value类型的内存数据库，很像memcached，整个数据库统统加载在内存当中进行操作，定期通过异步操作把数据库数据flush到硬盘上进行保存。

    因为是纯内存操作，Redis的性能非常出色，每秒可以处理超过 10万次读写操作，是已知性能最快的Key-Value DB。

    Redis的出色之处不仅仅是性能，Redis最大的魅力是支持保存多种数据结构，此外单个value的最大限制是1GB，不像 memcached只能保存1MB的数据，因此Redis可以用来实现很多有用的功能。

    比方说用他的List来做FIFO双向链表，实现一个轻量级的高性 能消息队列服务，用他的Set可以做高性能的tag系统等等。

    另外Redis也可以对存入的Key-Value设置expire时间，因此也可以被当作一 个功能加强版的memcached来用。 Redis的主要缺点是数据库容量受到物理内存的限制，不能用作海量数据的高性能读写，因此Redis适合的场景主要局限在较小数据量的高性能操作和运算上。
~~~

#### **13. 说说Redis哈希槽的概念？**
Redis集群没有使用一致性hash,而是引入了哈希槽的概念，Redis集群有16384个哈希槽，每个key通过CRC16校验后对16384取模来决定放置哪个槽，集群的每个节点负责一部分hash槽。

#### **14. Redis集群方案什么情况下会导致整个集群不可用？**
- 有A，B，C三个节点的集群,在没有复制模型的情况下,如果节点B失败了，那么整个集群就会以为缺少5501-11000这个范围的槽而不可用;

#### **15. Redis集群最大节点个数是多少？ Redis集群会有写操作丢失吗？为什么？**
- 16384个
- Redis并不能保证数据的强一致性，这意味这在实际中集群在特定的条件下可能会丢失写操作。

#### **16. Redis事务相关的命令有哪几个？**
- MULTI、EXEC、DISCARD、WATCH
#### **17. Redis回收进程如何工作的？Redis回收使用的是什么算法？**
- 一个客户端运行了新的命令，添加了新的数据。

Redi检查内存使用情况，如果大于maxmemory的限制, 则根据设定好的策略进行回收。

一个新的命令被执行，等等。



所以我们不断地穿越内存限制的边界，通过不断达到边界然后不断地回收回到边界以下。



如果一个命令的结果导致大量内存被使用（例如很大的集合的交集保存到一个新的键），不用多久内存限制就会被这个内存使用量超越。


- LRU算法
#### **32. Redis如何做大量数据插入？**
- Redis2.6开始redis-cli支持一种新的被称之为pipe mode的新模式用于执行大量数据插入工作。

#### **33. 为什么要做Redis分区？**

分区可以让Redis管理更大的内存，Redis将可以使用所有机器的内存。如果没有分区，你最多只能使用一台机器的内存。分区使Redis的计算能力通过简单地增加计算机得到成倍提升,Redis的网络带宽也会随着计算机和网卡的增加而成倍增长。


#### **34. 你知道有哪些Redis分区实现方案？**

客户端分区就是在客户端就已经决定数据会被存储到哪个redis节点或者从哪个redis节点读取。大多数客户端已经实现了客户端分区。



代理分区 意味着客户端将请求发送给代理，然后代理决定去哪个节点写数据或者读数据。代理根据分区规则决定请求哪些Redis实例，然后根据Redis的响应结果返回给客户端。redis和memcached的一种代理实现就是Twemproxy



查询路由(Query routing) 的意思是客户端随机地请求任意一个redis实例，然后由Redis将请求转发给正确的Redis节点。Redis Cluster实现了一种混合形式的查询路由，但并不是直接将请求从一个redis节点转发到另一个redis节点，而是在客户端的帮助下直接redirected到正确的redis节点。



#### **35. Redis分区有什么缺点？**

涉及多个key的操作通常不会被支持。例如你不能对两个集合求交集，因为他们可能被存储到不同的Redis实例（实际上这种情况也有办法，但是不能直接使用交集指令）。



同时操作多个key,则不能使用Redis事务.

分区使用的粒度是key，不能使用一个非常长的排序key存储一个数据集（The partitioning granularity is the key, so it is not possible to shard a dataset with a single huge key like a very big sorted set）.



当使用分区的时候，数据处理会非常复杂，例如为了备份你必须从不同的Redis实例和主机同时收集RDB / AOF文件。



分区时动态扩容或缩容可能非常复杂。Redis集群在运行时增加或者删除Redis节点，能做到最大程度对用户透明地数据再平衡，但其他一些客户端分区或者代理分区方法则不支持这种特性。然而，有一种预分片的技术也可以较好的解决这个问题。

#### **36. Redis持久化数据和缓存怎么做扩容？**

如果Redis被当做缓存使用，使用一致性哈希实现动态扩容缩容。



如果Redis被当做一个持久化存储使用，必须使用固定的keys-to-nodes映射关系，节点的数量一旦确定不能变化。否则的话(即Redis节点需要动态变化的情况），必须使用可以在运行时进行数据再平衡的一套系统，而当前只有Redis集群可以做到这样。

#### **37. 分布式Redis是前期做还是后期规模上来了再做好？为什么？**


既然Redis是如此的轻量（单实例只使用1M内存）,为防止以后的扩容，最好的办法就是一开始就启动较多实例。即便你只有一台服务器，你也可以一开始就让Redis以分布式的方式运行，使用分区，在同一台服务器上启动多个实例。



一开始就多设置几个Redis实例，例如32或者64个实例，对大多数用户来说这操作起来可能比较麻烦，但是从长久来看做这点牺牲是值得的。



这样的话，当你的数据不断增长，需要更多的Redis服务器时，你需要做的就是仅仅将Redis实例从一台服务迁移到另外一台服务器而已（而不用考虑重新分区的问题）。一旦你添加了另一台服务器，你需要将你一半的Redis实例从第一台机器迁移到第二台机器。

#### **38. Twemproxy是什么？**

Twemproxy是Twitter维护的（缓存）代理系统，代理Memcached的ASCII协议和Redis协议。

它是单线程程序，使用c语言编写，运行起来非常快。它是采用Apache 2.0 license的开源软件。 Twemproxy支持自动分区，如果其代理的其中一个Redis节点不可用时，会自动将该节点排除（这将改变原来的keys-instances的映射关系，所以你应该仅在把Redis当缓存时使用Twemproxy)。

Twemproxy本身不存在单点问题，因为你可以启动多个Twemproxy实例，然后让你的客户端去连接任意一个Twemproxy实例。

Twemproxy是Redis客户端和服务器端的一个中间层，由它来处理分区功能应该不算复杂，并且应该算比较可靠的。

#### **39. 查看Redis使用情况及状态信息用什么命令？**

info


#### **40. Redis的内存用完了会发生什么？**

如果达到设置的上限，Redis的写命令会返回错误信息（但是读命令还可以正常返回。）或者你可以将Redis当缓存来使用配置淘汰机制，当Redis达到内存上限时会冲刷掉旧的内容。

#### **41. Redis是单线程的，如何提高多核CPU的利用率？**
可以在同一个服务器部署多个Redis的实例，并把他们当作不同的服务器来使用，在某些时候，无论如何一个服务器是不够的， 所以，如果你想使用多个CPU，你可以考虑一下分片（shard）。

####**42. Redis常见性能问题和解决方案？**
(1) Master最好不要做任何持久化工作，如RDB内存快照和AOF日志文件

(2) 如果数据比较重要，某个Slave开启AOF备份数据，策略设置为每秒同步一次

(3) 为了主从复制的速度和连接的稳定性，Master和Slave最好在同一个局域网内

(4) 尽量避免在压力很大的主库上增加从库

(5) 主从复制不要用图状结构，用单向链表结构更为稳定，即：Master <- Slave1 <- Slave2 <- Slave3...

这样的结构方便解决单点故障问题，实现Slave对Master的替换。如果Master挂了，可以立刻启用Slave1做Master，其他不变。

####**43. Redis提供了哪几种持久化方式？**
- 参见基础 --
RDB持久化方式能够在指定的时间间隔能对你的数据进行快照存储。

AOF持久化方式记录每次对服务器写的操作,当服务器重启的时候会重新执行这些命令来恢复原始的数据,AOF命令以redis协议追加保存每次写的操作到文件末尾.Redis还能对AOF文件进行后台重写,使得AOF文件的体积不至于过大。



如果你只希望你的数据在服务器运行的时候存在,你也可以不使用任何持久化方式。



你也可以同时开启两种持久化方式, 在这种情况下, 当redis重启的时候会优先载入AOF文件来恢复原始的数据,因为在通常情况下AOF文件保存的数据集要比RDB文件保存的数据集要完整。



最重要的事情是了解RDB和AOF持久化方式的不同,让我们以RDB持久化方式开始。


#### **44. 如何选择合适的持久化方式？**

一般来说， 如果想达到足以媲美PostgreSQL的数据安全性， 你应该同时使用两种持久化功能。如果你非常关心你的数据， 但仍然可以承受数分钟以内的数据丢失，那么你可以只使用RDB持久化。



有很多用户都只使用AOF持久化，但并不推荐这种方式：因为定时生成RDB快照（snapshot）非常便于进行数据库备份， 并且 RDB 恢复数据集的速度也要比AOF恢复的速度要快，除此之外， 使用RDB还可以避免之前提到的AOF程序的bug。



#### **45、修改配置不重启Redis会实时生效吗？**
针对运行实例，有许多配置选项可以通过 CONFIG SET 命令进行修改，而无需执行任何形式的重启。



从 Redis 2.2 开始，可以从 AOF 切换到 RDB 的快照持久性或其他方式而不需要重启 Redis。检索 ‘CONFIG GET *’ 命令获取更多信息。


但偶尔重新启动是必须的，如为升级 Redis 程序到新的版本，或者当你需要修改某些目前 CONFIG 命令还不支持的配置参数的时候。


#### **46. redis热启动**


#### **47. 多个线程同时访问为空的redis，怎么解决(缓存更新, 重建的问题)**