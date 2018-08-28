from random import randint
import time 
# 插入排序 始终保持前面是有序的
"""
    1. 从第一个元素开始，该元素可以认为已经被排序
    2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
    3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
    4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
    5. 将新元素插入到该位置后
    6. 重复步骤2~5
"""


def insert_sort(alist):
    length = len(alist)
    for i in range(1, length):
        elem = alist[i]
        j = i
        while elem < alist[j-1]:
            alist[j] = alist[j-1]
            j -= 1
            if j < 1:
                break
        alist[j] = elem
    return 


if __name__ == "__main__":
    n = 10
    while n:
        rec = []
        for i in range(10000):
            rec.append(randint(0, 10000))
        res = list(rec)
            
        t0 = time.time()
        insert_sort(rec)
        t1 = time.time()
        print("my_insertion_sort runs: %.8f"%(t1-t0))

        t2 = time.time()
        ret = sorted(res)
        t3 = time.time()
        print("Python sorted runs: %.8f"%(t3-t2))

        print("my sort runs ok: ", rec == ret)
        print("="*50)
        n -= 1