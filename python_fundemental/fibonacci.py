'''
斐波那契数列，要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''
#fibonacci 数列: 1,1,2,3,5,8,13,21......
from datetime import datetime

# 题9

#此方法, 计算fibonacci(40) 需24.902843952178955秒
def fibonacci(n):
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_by_rec(n):
    """青蛙跳同理"""
    if n <= 2:
        return 1
    temp = [1, 1]
    for i in range(3, n+1):
        temp[i%2] = temp[0] + temp[1]
    return temp[n%2]

    


if __name__ == '__main__':
    start_time = datetime.now().timestamp()
    a = fibonacci_by_rec(8)
    end_time = datetime.now().timestamp()
    print(a)
    print(end_time-start_time)