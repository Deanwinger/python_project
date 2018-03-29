from time import sleep, strftime
from concurrent import futures

def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)

def loiter(n):
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t'*n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t'*n, n))
    return n * 10

def main():
    display('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, range(5))
    display('results:', results)
    display('Waiting for individual results:')
    # for 循环中的 enumerate 函数会隐式调用 next(results),这个
    # 函数又会在(内部)表示第一个任务(loiter(0))的 _f 期物上调
    # 用_f.result() 方法。result 方法会阻塞,直到期物运行结束,
    # 因此这个循环每次迭代时都要等待下一个结果做好准备
    for i, result in enumerate(results):
        display('result {}: {}'.format(i, result))

if __name__ == '__main__':
    main()