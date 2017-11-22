import os
import time
from multiprocessing import Process


def main():
    print("I am the parent process")
    p = Process(target=run_proc, args=('John',))
    p.start()
    p.join()
    print('after 5 seconds, still me')

def run_proc(name):
    n=0
    print('Run child process %s (%s)...' % (name, os.getpid()))
    while n <5:
        n += 1
        print("countdown: " + str(n))
        time.sleep(1)

# os.system()成功则返回0
def run():
    # os.chdir('/home/ubuntu/src/LS-API')
    os.chdir('/home/ubuntu/alan/python_related')
    # os.system("git pull origin master")
    s = os.system("git status")
    print("The success return code: ", s)
    e = os.system("got status")
    print("The failure return code: ", e)
    print("The current process id %s" % os.getpid())

# 显示如下
# 位于分支 master
# 尚未暂存以备提交的变更：
#   （使用 "git add <file>..." 更新要提交的内容）
#   （使用 "git checkout -- <file>..." 丢弃工作区的改动）

#     修改：     python_reload/autoreload.py

# 未跟踪的文件:
#   （使用 "git add <file>..." 以包含要提交的内容）

#     python_fundemental/multiprocess_related.py
#     python_reload/__pycache__/

# 修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
# The success return code:  0
# sh: 1: got: not found
# The failure return code:  32512
# The current process id 28501




if __name__ == '__main__':
    main()
    # run()