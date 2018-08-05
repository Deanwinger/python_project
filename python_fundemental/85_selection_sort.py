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


if __name__ == "__main__":
    # a = [1,4,7,6,9,2,5,8]
    # b = list(a)
    # select_sort(a)
    # print(a)

    # print(sorted(b))

    n = 30
    while n:
        ori = rec = []
        for i in range(10000):
            rec.append(randint(0, 10000))
        res = list(rec)
            
        t0 = time.time()
        select_sort(rec)
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