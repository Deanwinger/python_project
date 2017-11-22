from pprint import pprint
from daemonize import daemonize
from multiprocessing import Process
import os
import time

# 方案: Python开源的Web框架（Django、Flask等）都有自己的自动加载模块功能（autoreload.py）
# subprocess模式创建子进程，主进程作为守护进程，子进程中一个线程负责检测文件是否发生变化，
# 如果发生变化则退出，主进程检查子进程的退出码（exist code）如果与约定的退出码一致，
# 则重新启动一个子进程继续工作。
 
root = "/home/ubuntu/src/LS-API"
# 主进程做守护进程, 每嗝2秒检测文件是否发生变化(git pull)
# 如果发生了变化 uwsgi stop, 然后reload, 然后fab deploy
def change_detector():
    daemonize()
    # signal.signal(signal.SIGTERM, _signal_handler)
    #创建子进程,需切换到~src/LS_API下执行
    while 1:
        is_changed = _is_any_file_changed()
        if is_changed:
            #执行uwsgi stop
            process_stop = subprocess.Popen(
                    "git pull origin master", 
                    cwd=root, 
                    shell=True, 
                    stdout=subprocess.PIPE, 
                    close_fds=True)
            process_stop.wait()
            #再执行uwsgi init
            process_init = subprocess.Popen("uwsgi uwsgi.ini --daemonize uwsgi.log --pidfile /tmp/uwsgi.pi", 
                    cwd=root, 
                    shell=True, 
                    stdout=subprocess.PIPE, 
                    close_fds=True)
            process_init.wait()
        time.sleep(5)

def daemonize():
    # 从父进程fork一个子进程出来
    pid = os.fork()

    if pid:
        # 退出父进程，sys.exit()方法比os._exit()方法会多执行一些刷新缓冲工作
        sys.exit(0)

    # 子进程默认继承父进程的工作目录，最好是变更到根目录，否则会影响文件系统的卸载
    os.chdir('/')
    # 子进程默认继承父进程的umask（文件权限掩码），重设为0（完全控制），以免影响程序读写文件
    os.umask(0)
    # 让子进程成为新的会话组长和进程组长
    os.setsid()

    # 第2次fork，也就是子进程的子进程
    _pid = os.fork()
    if _pid:
        # 退出子进程
        sys.exit(0)

    # 此时，孙子进程已经是守护进程了，接下来重定向标准输入、输出、
    # 错误的描述符(是重定向而不是关闭, 这样可以避免程序在 print 的时候出错)

    # 刷新缓冲区先，小心使得万年船
    sys.stdout.flush()
    sys.stderr.flush()

        # dup2函数原子化地关闭和复制文件描述符，重定向到/dev/nul，即丢弃所有输入输出
    with open('/dev/null') as read_null, open('/dev/null', 'w') as write_null:
        os.dup2(read_null.fileno(), sys.stdin.fileno())
        os.dup2(write_null.fileno(), sys.stdout.fileno())
        os.dup2(write_null.fileno(), sys.stderr.fileno())



def _is_any_file_changed():
    #执行git pull
    process_pull = subprocess.Popen(
            "git pull origin master", 
            cwd=root, 
            shell=True, 
            stdout=subprocess.PIPE, 
            close_fds=True)
    out = process_pull.stdout.read()
    print(out.decode('utf-8'))
    process_pull.wait()
    #遍历







if __name__ == '__main__':
    # change_detector()
    subprocess_run()