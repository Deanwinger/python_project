
`IOLoop模块 + Gen模块`

1. 如何理解Tornado中的协程模块?
`https://blog.csdn.net/wyx819/article/details/45420017`
`https://segmentfault.com/a/1190000004373224`
tornado的coroutine跟greenlet略有区别，跟asyncio里的协程类似。本质上来说只是把本来需要拆成多个callback的代码合进了一个生成器，生成器不断yield一系列的Future对象，调度器在Future完成时通过调用生成器的send方法唤醒协程，实现执行-等待-执行-等待的逻辑，而从全局看，所有协程共享一个线程，一个协程等待的时候调度器会插入其他协程进行执行。通过gen修饰的协程本身也会返回一个Future，这个Future在协程返回时完成，等待这个Future就可以达到等待协程执行结束的效果。
