# MySQL_缓存相关
`缓存相关`


#### **28. 在极端情况下，系统缓存全部失效，该如何防止流量全部打到数据库上**
`缓存重建问题`
`相关问题--redis开发与运维都有涉及`
-面对cache aside可能出现的全部打在数据库的情况， 比较简单的方式就是预热，可以用脚本来提前写入到 cache 热缓存。或者改用缓存策略， 使用Write-Through 直接写缓存，然后更新到数据库。

- 这个问题可以用一些可以提供持久化功能的缓存来实现，比如Redis，在未开启aof的情况下，其定期dump出来的rdb文件出能自动恢复出绝大部分数据；

- 而MongoDB与上面的方式不太一样，MongoDB采用mmap来将数据文件映射到内存中，所以当MongoDB重启时，这些映射的内存并不会清掉，因为它们是由操作系统维护的（所以当操作系统重启时，MongoDB才会有相同问题）。相对于其它一些自己维护Cache的数据库，MongoDB在重启后并不需要进行缓存重建与预热；

- 另外，新浪微博的timyang也曾经提出过一种缓存重建加锁的方式，也能部分解决此问题。简单来说就是缓存重建时，当多个客户端对同一个缓存数据发起请求时，会在客户端采用加锁等待的方式，对同一个Cache的重建需要获取到相应的锁才行，只有一个客户端能拿到锁，并且只有拿到锁的客户端才能访问数据库重建缓存，其它的客户端都需要等待这个拿到锁的客户端重建好缓存后直接读缓存，其结果是对同一个缓存数据，只进行一次数据库重建访问。但是如果访问分散比较严重，还是会瞬间对数据库造成非常大的压力。


#### **34. 缓存更新 策略**
`https://coolshell.cn/articles/17416.html`
`https://zhuanlan.zhihu.com/p/59167071`

- 错误实践: 先删缓存,然后再更新数据库;
~~~
    1. 两个并发操作, 如果一个读请求和一个更新请求, 写请求先删了缓存, 而读请求直接去数据库拿数据, 在数据库更新之前拿到就是原来的旧数据, 然后放入缓存, 此时写请求完成, 最后缓存中的数据是原来的数据(脏数据)
~~~

- 一. Cache Aside
~~~
    1. 最最常用的pattern, 逻辑如下:
        失效: 应用程序先从Cache取数据, 没有取到, 则从数据库取, 成功后, 放入缓存;
        命中: 应用程序直接从Cache获取数据, 返回;
        更新: 先把数据存到数据库中, 成功后, 再让缓存失效;

    注意，我们的更新是先更新数据库，成功后，让缓存失效。那么，这种方式是否可以没有文章前面提到过的那个问题呢？我们可以脑补一下。

    一个是查询操作，一个是更新操作的并发，首先，没有了删除cache数据的操作了，而是先更新了数据库中的数据，此时，缓存依然有效，所以，并发的查询操作拿的是没有更新的数据，但是，更新操作马上让缓存的失效了，后续的查询操作再把数据从数据库中拉出来。而不会像文章开头的那个逻辑产生的问题，后续的查询操作一直都在取老的数据。

    这是标准的design pattern，包括Facebook的论文《Scaling Memcache at Facebook》也使用了这个策略。为什么不是写完数据库后更新缓存？你可以看一下Quora上的这个问答《Why does Facebook use delete to remove the key-value pair in Memcached instead of updating the Memcached during write request to the backend?》，主要是怕两个并发的写操作导致脏数据。

    那么，是不是Cache Aside这个就不会有并发问题了？不是的，比如，一个是读操作，但是没有命中缓存，然后就到数据库中取数据，此时来了一个写操作，写完数据库后，让缓存失效，然后，之前的那个读操作再把老的数据放进去，所以，会造成脏数据。

    但，这个case理论上会出现，不过，实际上出现的概率可能非常低，因为这个条件需要发生在读缓存时缓存失效，而且并发着有一个写操作。而实际上数据库的写操作会比读操作慢得多，而且还要锁表，而读操作必需在写操作前进入数据库操作，而又要晚于写操作更新缓存，所有的这些条件都具备的概率基本并不大。

    所以，这也就是Quora上的那个答案里说的，要么通过2PC或是Paxos协议保证一致性，要么就是拼命的降低并发时脏数据的概率，而Facebook使用了这个降低概率的玩法，因为2PC太慢，而Paxos太复杂。当然，最好还是为缓存设置上过期时间。
~~~

- 二. Read/Write through -- 细节不完善
~~~
    1. 逻辑如下:
        命中: 直接获取数据;
        失效: 从数据库读取数据进缓存, 然后从缓存返回数据给调用者;
        更新:
            a. 如果没有命中缓存, 则直接更新数据库, 然后返回;
            b. 如果命中了缓存, 则更新缓存, 然后由Cache自己更新数据库(这是一个同步操作);

    The application uses the cache as the main data store, reading and writing data to it, while the cache is responsible for reading and writing to the database:
        Application adds/updates entry in cache
        Cache synchronously(同步) writes entry to data store
        Return

    Disadvantage(s): 
        write throughWhen a new node is created due to failure or scaling, the new node will not cache entries until the entry is updated in the database. Cache-aside in conjunction with write through can mitigate this issue

~~~

- 四. Write behind caching
~~~
    1. Write Behind 又叫 Write Back, 在更新数据的时候，只更新缓存，不更新数据库，而我们的缓存会异步地批量更新数据库。
    2. 一些了解Linux操作系统内核的同学对write back应该非常熟悉，这不就是Linux文件系统的Page Cache的算法吗?
    
    流程: In write-behind, the application does the following:
    Add/update entry in cache
    Asynchronously write entry to the data store, improving write performance

    Disadvantage(s): write-behind
        There could be data loss if the cache goes down prior to its contents hitting the data store.
        It is more complex to implement write-behind than it is to implement cache-aside or write-through.


~~~


#### **79. 如果缓存失效，瞬间大量请求可能会直接访问数据库(缓存雪崩)**
- 
~~~
    均匀分布 : 我们应该在设置失效时间时应该尽量均匀的分布,比如失效时间是当前时间加上一个时间段的随机值;
    熔断机制 : 类似于SpringCloud的熔断器,我们可以设定阈值或监控服务,如果达到熔断阈值(QPS,服务无法响应,服务超时)时,则直接返回,不再调用目标服务,并且还需要一个检测机制,如果目标服务已经可以正常使用,则重置阈值,恢复使用;
    隔离机制 : 类似于Docker一样,当一个服务器上某一个tomcat出了问题后不会影响到其它的tomcat,这里我们可以使用线程池来达到隔离的目的,当线程池执行拒绝策略后则直接返回,不再向线程池中增加任务;
    限流机制 : 其实限流就是熔断机制的一个版本,设置阈值(QPS),达到阈值之后直接返回;

    facebook 放过一篇论文《Scaling Memcache at Facebook》有讨论过这个问题：
        3.2.1 LeasesWe introduce a new mechanism we call leases to address two problems: stale sets and thundering herds.
        
    其中 "thundering herds" 正是楼主提到的数据库穿透问题，一个热的缓存如果失效，在第一个访问数据库的请求得到结果写入缓存之前，期间的大量请求打穿到数据库；
    然后 “stale set” 属于数据一致性问题，假如一个实例更新了数据想去刷新缓存，而另一个实例读 miss 尝试读取数据库，这时两次缓存写入顺序不能保证，可能会导致过期数据写入缓存。
    
    这两个问题都是 look-aside cache 所固有的，需要提供一个机制来协调缓存的写入，这篇论文给出的方案就是 lease 机制，限制同一时刻一个键只有拥有唯一 lease 的客户端才能有权写入缓存：
        1. 如果 get 某键读 miss，返回客户端一个 64 位的 lease；
        2. 然后该键在写入之前如果收到 get 请求，将返回一个 hot miss 报错，客户端依据它判断自己要稍后重试，而不向数据库读取数据；
        3. 如果该键收到 delete 请求，那么会使 lease 失效；持有失效 lease 的 set 请求仍将成功，但后来的 get 请求将得到 hot miss 报错，并携带一个新的 lease；这里的 hot miss 报错中带有最后的值，但认为它处于 stale 状态，留给客户端去判断是否采用它，在一致性要求不严格的场景中可以进一步减少数据库请求；

    这一来允许 memcache 服务端协调数据库的访问，从而解决这两个问题。不过 lease 方案并不完美，因为 1. 需要改 memcache；2. 仍泄露逻辑到客户端，要求客户端遵循 lease 和 hot miss 的约定。
    在 facebook 后面的论文《TAO: Facebook's Distributed Data Store for the Social Graph》中介绍TAO 系统尝试解决的问题之一提到：
    Distributed control logic: In a lookaside cache architecture
        the control logic is run on clients that don’t communicate
        with each other. This increases the number of
        failure modes, and makes it difficult to avoid thundering
        herds. Nishtala et al. provide an in-depth discussion of
        the problems and present leases, a general solution [21].
        For objects and associations the fixed API allows us to
        move the control logic into the cache itself, where the
        problem can be solved more efficiently.
    也就是说，我们并不一定非 look aside cache 不可，如果把缓存的修改入口封装起来，走 write though cache，就不需要分布式地去协调所有客户端，在一个地方排队就够了。
~~~

#### **80. 缓存穿透**
- 发生场景 : 此时要查询的数据不存在,缓存无法命中所以需要查询完数据库,但是数据是不存在的,此时数据库肯定会返回空,也就无法将该数据写入到缓存中,那么每次对该数据的查询都会去查询一次数据库

~~~
    解决方案 : 
        布隆过滤 : 我们可以预先将数据库里面所有的key全部存到一个大的map里面,然后在过滤器中过滤掉那些不存在的key.但是需要考虑数据库的key是会更新的,此时需要考虑数据库 --> map的更新频率问题;BloomFilter 类似于一个hbase set 用来判断某个元素（key）是否存在于某个集合中;
        缓存空值 : 哪怕这条数据不存在但是我们任然将其存储到缓存中去,设置一个较短的过期时间即可,并且可以做日志记录,寻找问题原因;
~~~