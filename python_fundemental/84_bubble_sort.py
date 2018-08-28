# 冒泡排序
"""
冒泡排序算法的原理如下：
    1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    2. 对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
    3. 针对所有的元素重复以上的步骤，除了最后一个。
    4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
"""

from random import randint
import time 


def bubble_sort(alist):
    length = len(alist)
    for i in range(length): # 这一行代码的含义是, 每次只能保证最大的那一个移到后面去
        found = False
        for j in range(1, length-i):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
                found = True
        if not found:
            break
    return


if __name__ == "__main__":
    n = 30
    while n:
        rec = []
        for i in range(10000):
            rec.append(randint(0, 10000))
        res = list(rec)
            
        t0 = time.time()
        bubble_sort(rec)
        t1 = time.time()
        print("my_insertion_sort runs: %.8f"%(t1-t0))

        t2 = time.time()
        ret = sorted(res)
        t3 = time.time()
        print("Python sorted runs: %.8f"%(t3-t2))

        print("my sort runs ok: ", rec == ret)
        if rec != ret:
            raise Exception("Whoops, you got it wrong: ", ori)
        print("="*50)
        n -= 1