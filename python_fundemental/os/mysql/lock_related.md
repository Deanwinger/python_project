# MySQL_LOCK
`锁相关`

#### **1. MySQL锁有几种**
`https://www.aneasystone.com/archives/2017/11/solving-dead-locks-two.html`
`上篇文章总结的很好, to be finished`
~~~
    表／行／页-锁：
        表级锁（table-level locking）：MyISAM和MEMORY存储引擎
        行级锁（row-level locking） ：InnoDB存储引擎
        页面锁（page-level-locking）：BDB存储引擎

        表级锁：开销小，并发低，加锁快；不会出现死锁；锁定粒度大，发生锁冲突的概率最高,并发度也最低。
        行级锁：开销大，并发高，加锁慢；会出现死锁；锁定粒度最小，发生锁冲突的概率最低,并发度也最高。
        页面锁：开销和加锁时间界于表锁和行锁之间；会出现死锁；锁定粒度界于表锁和行锁之间，并发度一般。

    共享／排他锁
        共享锁又称读锁，是读取操作创建的锁。其他用户可以并发读取数据，但任何事务都不能对数据进行修改（获取数据上的排他锁），直到已释放所有共享锁。
        排他锁又称写锁，如果事务T对数据A加上排他锁后，则其他事务不能再对A加任任何类型的封锁。获准排他锁的事务既能读数据，又能修改数据。

    Mysiam锁模式
        MyISAM在执行查询语句（SELECT）前，会自动给涉及的所有表加读锁，在执行更新操作（UPDATE、DELETE、INSERT等）前，会自动给涉及的表加写锁。
        a、对MyISAM表的读操作(加读锁),不会阻塞其他进程对同一表的读请求,但会阻塞对同一表的写请求.只有当读锁释放后才会执行其它进程的写操作。
        b、对MyISAM表的写操作(加写锁),会阻塞其他进程对同一表的读和写操作，只有当写锁释放后，才会执行其它进程的读写操作。

    innodb锁模式
        意向锁是InnoDB自动加的，不需要用户干预。
        对于insert、update、delete，InnoDB会自动给涉及的数据加排他锁（X）；对于一般的Select语句，InnoDB不会加任何锁，事务可以通过以下语句给显示加共享锁或排他锁。
        共享锁： SELECT ... LOCK IN SHARE MODE;
        排他锁： SELECT ... FOR UPDATE;
~~~

#### **70. 死锁是怎么产生的**
`死锁四个必要条件`
#### **71. 死锁问题的分析和解决**
`https://www.aneasystone.com/archives/2018/04/solving-dead-locks-four.html`
#### **72. 常见 SQL 语句的加锁分析**
`https://www.aneasystone.com/archives/2017/12/solving-dead-locks-three.html`


#### **95.用个通俗的例子讲一讲死锁**
`https://zhuanlan.zhihu.com/p/26945588`