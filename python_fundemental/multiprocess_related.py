import os
import time
from multiprocessing import Process
import subprocess


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

# os.system if success return 0
def run():
    os.chdir('/home/ubuntu/alan/python_related')
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

#subproces的使用
def run2():
    print("I am father process(%s)..." % os.getpid())
    cmd = "ls -l"
    p1 = subprocess.Popen(cmd, cwd="/home/ubuntu/alan/python_related/python_fundemental", 
                        shell=True, stdout=subprocess.PIPE)
    p2 = subprocess.Popen("python test.py", cwd="/home/ubuntu/alan/python_related/python_fundemental", 
                    shell=True, stdin=p1.stdout, stdout=subprocess.PIPE)
    out = p2.stdout.read()
    print(out.decode('utf-8'))
    s1 = p1.wait()
    s2 = p2.wait()
    print("============", s1,s2,p1.returncode, p2.returncode, "=============")
    print("Main process done")



if __name__ == '__main__':
    # main()
    # run()
    run2()