import threading
import itertools
import time
import sys

def display(*args):
    print(time.strftime('[%H:%M:%S]'), end=' ')
    print(*args)

class Signal:
    go = True

def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08'*len(status))#光标回退
        time.sleep(.1)
        if not signal.go:
            break
    write(' ' * len(status) + '\x08' * len(status)) #使用空格清除状态消息,把光标移回开头。

def slow_function():
    # 假装等待I/O一段时间
    time.sleep(3)
    return 42

def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, 
                                args=('thinking!', signal))
    print('spinner object:', spinner)
    spinner.start()
    result = slow_function()
    signal.go = False
    spinner.join()
    return result

def main():
    t0 = time.time()
    result = supervisor()
    total = time.time() - t0
    # print('total_time: ', total)
    print('Answer:', result)



if __name__ == '__main__':
    main()
