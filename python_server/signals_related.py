"""
    对应于unix网络编程 -- 信号处理
    Linux系统编程 20.4 有介绍
    关于信号处理的逻辑流

    内核处理一个进程收到的软中断信号是在该进程的上下文中，因此，进程必须处于运行状态。前面介绍概念的时候讲过，
    处理信号有三种类型：进程接收到信号后退 出；进程忽略该信号；进程收到信号后执行用户设定用系统调用signal的函数。
    当进程接收到一个它忽略的信号时，进程丢弃该信号，就象没有收到该信号似 的继续运行。如果进程收到一个要捕捉的信号，
    那么进程从内核态返回用户态时执行用户定义的函数。而且执行用户定义的函数的方法很巧妙，内核是在用户栈上创 建一个新的层，
    该层中将返回地址的值设置成用户定义的处理函数的地址，这样进程从内核返回弹出栈顶时就返回到用户定义的函数处，
    从函数返回再弹出栈顶时， 才返回原先进入内核的地方。这样做的原因是用户定义的处理函数不能且不允许在内核态下执行
    （如果用户定义的函数在内核态下运行的话，用户就可以获得任何权限）

"""

import signal
import os


def sig_chld(signo):
    # 用于处理 信号 SIGCHLD, 子进程在退出的时候会给其父进程发送一个SIGCHILD信号以告诉父进程"我已经退出了
    # os.waitpid(pid, options), If pid is -1, the request pertains to any child of the current process
    # The option for waitpid() to return immediately if no child process status is available immediately. The function returns (0, 0) in this case
    waitpid(-1, os.WNOHANG)
    print('I received: ', signo)

