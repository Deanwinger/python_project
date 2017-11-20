import os,sys,time,subprocess,threading,signal
from pprint import pprint
from imp import reload

# 方案: Python开源的Web框架（Django、Flask等）都有自己的自动加载模块功能（autoreload.py）
# subprocess模式创建子进程，主进程作为守护进程，子进程中一个线程负责检测文件是否发生变化，
# 如果发生变化则退出，主进程检查子进程的退出码（exist code）如果与约定的退出码一致，
# 则重新启动一个子进程继续工作。


# .pyc是一种二进制文件，是由py文件经过编译后，生成的文件，是一种byte code，
# py文件变成pyc文件后，加载的速度有所提高，而且pyc是一种跨平台的字节码，
# 是由python的虚拟机来执行的，这个是类似于JAVA或者.NET的虚拟机的概念。
# pyc的内容，是跟python的版本相关的，不同版本编译后的pyc文件是不同的，
# 2.5编译的pyc文件，2.4版本的 python是无法执行的。

# .pyo是优化编译后的程序 python -O 源文件即可将源程序编译为pyo文件 

def _iter_module_files():
    alist = []
    # pprint(list(sys.modules))
    # pprint(list(sys.modules.values()))
    for module in list(sys.modules.values()):
        filename = getattr(module, '__file__', None)
        # alist.append(filename)
        # pprint(alist, indent=4)
        if filename:
            # print("==========================*")
            if filename[-4:] in ('.pyo', '.pyc'):
                # print("===========================")
                filename = filename[:-1]
                # pprint(filename)
            # yield filename

def _is_any_file_changed(mtimes):
    """Return 1 if there is any source file of sys.modules changed,
    otherwise 0. mtimes is dict to store the last modify time for
    comparing."""
    for filename in _iter_module_files():
        try:
            mtime = os.stat(filename).st_mtime
        except IOError:
            continue
        old_time = mtimes.get(filename, None)
        if old_time is None:
            mtimes[filename] = mtime
        elif mtime > old_time:
            pprint(mtimes)
            return 1
    return 0

def _start_change_detector(interval = 1):
    """Check file state ervry interval. If any change is detected, exit this
    process with a special code, so that deamon will to restart a new process.
    """
    mtimes = {}
    while 1:
        if _is_any_file_changed(mtimes):
            sys.exit(3)
        time.sleep(1)


# current subprocess
_sub_proc = None

def _signal_handler(*args):
    """Signal handler for process terminated. If there is a subprocess, 
    terminate it firstly."""
    global _sub_proc
    if _sub_proc:
        _sub_proc.terminate()
    sys.exit(0)


def _restart_with_reloader():
    """Deamon for subprocess."""
    signal.signal(signal.SIGTERM, _signal_handler)
    while 1:
        args = [sys.executable] + sys.argv
        new_env['RUN_FLAG'] = 'true'
        global _sub_proc
        _sub_proc = subprocess.Popen(args, env=new_env, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        _ridrect_stdout(_sub_proc.stdout)
        exit_code = _sub_proc.wait()
        if exit_code != 3:
            return exit_code


def _ridrect_stdout(stdout):
    """Redirect stdout to current stdout."""
    while 1:
        data = os.read(stdout.fileno(), 2**15)
        if len(data) > 0:
            sys.stdout.write(data)
        else:
            stdout.close()
            sys.stdout.flush()
            break




if __name__ == '__main__':
    mtimes={}
    _is_any_file_changed(mtimes)