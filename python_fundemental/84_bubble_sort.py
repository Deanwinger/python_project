# 冒泡排序

from random import randint
import time 


def bubble_sort(alist):
    length = len(alist)
    for i in range(length):
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