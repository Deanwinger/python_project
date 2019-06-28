"""
简单选择排序的基本思想：给定数组：int[] arr={里面n个数据}；第1趟排序，
在待排序数据arr[1]~arr[n]中选出最小的数据，将它与arrr[1]交换；第2趟，
在待排序数据arr[2]~arr[n]中选出最小的数据，将它与r[2]交换；以此类推，
第i趟在待排序数据arr[i]~arr[n]中选出最小的数据，将它与r[i]交换，直到全部排序完成。
"""


# 选择排序
from random import randint
import time


def select_sort(alist):
    length = len(alist)
    for i in range(length):
        cur = i
        for j in range(i, length):
            if alist[j] < alist[cur]:
                cur = j
        alist[i], alist[cur] = alist[cur], alist[i]
    return 

# 2019-6-28 选择排序, 同样保证前面是有序的, 一次选出第一个位置, 第二个位置的元素...
def ssort(alist):
    n = len(alist)
    for i in range(n):
        cur = i
        for j in range(i+1, n):
            if alist[j]<alist[cur]:
                cur = j
        alist[i], alist[cur] = alist[cur], alist[i]
    return
                

if __name__ == "__main__":
    # a = [1,4,7,6,9,2,5,8]
    # b = list(a)
    # select_sort(a)
    # print(a)

    # print(sorted(b))

    n = 30
    while n:
        ori = rec = []
        for i in range(1000):
            rec.append(randint(0, 1000))
        res = list(rec)
            
        t0 = time.time()
        ssort(rec)
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