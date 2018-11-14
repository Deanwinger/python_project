"""
    对应于unix网络编程 -- 信号处理
"""

import signal


def sig_chld(signo):
    # TODO wait 函数待补充
    # 用于处理 信号 SIGCHLD, 子进程在退出的时候会给其父进程发送一个SIGCHILD信号以告诉父进程"我已经退出了
    print('I received: ', signo)

