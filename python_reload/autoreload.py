# 方案: Python开源的Web框架（Django、Flask等）都有自己的自动加载模块功能（autoreload.py）
# subprocess模式创建子进程，主进程作为守护进程，子进程中一个线程负责检测文件是否发生变化，
# 如果发生变化则退出，主进程检查子进程的退出码（exist code）如果与约定的退出码一致，
# 则重新启动一个子进程继续工作。

import os
import sys

import atexit
import signal

import subprocess


def daemonize(pidfile, *, stdin='/dev/null',
                          stdout='/dev/null',
                          stderr='/dev/null'):
    if os.path.exists(pidfile):
        raise RuntimeError('Already running')

    # First fork (detaches from parent)
    try:
        if os.fork() > 0:
            #sys.exit(0)函数会正常关闭解释器
            raise SystemExit(0)
    except OSError as e:
        raise RuntimeError('fork #1 failed.')

    os.chdir('/')
    os.umask(0)
    os.setsid()

    # Second fork (relinquish session leadership)
    try:
        if os.fork() > 0:
            raise SystemExit(0)
    except OSError as e:
        raise RuntimeError('fork #2 failed.')

    # Flush I/O buffers
    sys.stdout.flush()
    sys.stderr.flush()

    # Replace file descriptors for stdin, stdout, and stderr
    with open(stdin, 'rb', 0) as f:
        os.dup2(f.fileno(), sys.stdin.fileno())
    with open(stdout, 'ab', 0) as f:
        os.dup2(f.fileno(), sys.stdout.fileno())
    with open(stderr, 'ab', 0) as f:
        os.dup2(f.fileno(), sys.stderr.fileno())

    # Write the PID file
    with open(pidfile,'w') as f:
        print(os.getpid(),file=f)

    atexit.register(lambda: os.remove(pidfile))

    # SIGTERM的信号处理器, 简单的抛出了 SystemExit() 异常。 
    # 如果没有它，终止信号会使得不执行 atexit.register() 注册的清理操作的时候就杀掉了解释器。
    def sigterm_handler(signo, frame):
        raise SystemExit(1)

    signal.signal(signal.SIGTERM, sigterm_handler)

def main():
    import time
    sys.stdout.write('Daemon started with pid {}\n'.format(os.getpid()))
    while True:
        sys.stdout.write('Daemon Alive! {}\n'.format(time.ctime()))
        time.sleep(5)


def detect_changes():
    # signal.signal(signal.SIGTERM, _signal_handler)
    #创建子进程,需切换到~src/LS_API下执行
    import time
    sys.stdout.write('Daemon(LS-API) started with pid {}\n'.format(os.getpid()))
    mtimes = {}
    while 1:
        is_changed = _is_any_file_changed(mtimes)
        if is_changed:
            #执行uwsgi stop 
            # print(mtimes)
            # process_stop = subprocess.Popen(
            #         "git pull origin master", 
            #         cwd=root, 
            #         shell=True, 
            #         stdout=subprocess.PIPE, 
            #         close_fds=True)
            # out = process_pull.stdout.read()
            # print(out.decode('utf-8'))
            # process_stop.wait()
            #再执行uwsgi init
            # process_init = subprocess.Popen("uwsgi uwsgi.ini --daemonize uwsgi.log --pidfile /tmp/uwsgi.pi", 
            #         cwd=root, 
            #         shell=True, 
            #         stdout=subprocess.PIPE, 
            #         close_fds=True)
            # process_init.wait()
            sys.stdout.write('Yoour changed your file! {}\n'.format(time.ctime()))
        sys.stdout.write('Daemon Alive! {}\n'.format(time.ctime()))
        time.sleep(5)

def _is_any_file_changed(mtimes):
    root = "/home/ubuntu/alan/python_related"
    # root = "/home/ubuntu/alan/gitlab/LS-API"
    #执行git pull
    # process_pull = subprocess.Popen(
    #         "git pull origin master", 
    #         cwd=root, 
    #         shell=True, 
    #         stdout=subprocess.PIPE, 
    #         close_fds=True)
    # out = process_pull.stdout.read()
    # sys.stdout.write(out.decode('utf-8'))
    # s1 = process_pull.wait()
    #遍历
    for i in os.walk(root):
        for s in i[2]:
            filename = str(i[0]) + '/' + str(s)
            try:
                file_time = os.stat(filename).st_mtime
            except IOError:
                continue
            old_time = mtimes.get(filename, None)
            if old_time is None:
                mtimes[filename] = file_time
            elif file_time > old_time:
                mtimes[filename] = file_time
                # sys.stdout.write("Here is the trouble one %s" % filename )
                return 1
    return 0
            

if __name__ == '__main__':
    PIDFILE = '/tmp/daemon.pid'

    if len(sys.argv) != 2:
        print('Usage: {} [start|stop]'.format(sys.argv[0]), file=sys.stderr)
        raise SystemExit(1)

    if sys.argv[1] == 'start':
        try:
            daemonize(PIDFILE,
                      stdout='/tmp/daemon.log',
                      stderr='/tmp/daemon.log')
        except RuntimeError as e:
            print(e, file=sys.stderr)
            raise SystemExit(1)

        detect_changes()

    elif sys.argv[1] == 'stop':
        if os.path.exists(PIDFILE):
            with open(PIDFILE) as f:
                os.kill(int(f.read()), signal.SIGTERM)

    else:
        print('Unknown command {!r}'.format(sys.argv[1]), file=sys.stderr)
        raise SystemExit(1)