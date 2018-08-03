# 快速排序

from random import randint
import time 

"""
    basic plan:
        1. Shuffle the array
        2. partition
        3. sort
"""

def quick_sort(nums, lo, hi): 
    if lo >= hi:
        return 
    j = partition(nums, lo, hi)
    quick_sort(nums, 0, j-1)
    quick_sort(nums, j+1, hi)
    return nums

def partition(nums, lo: int, hi: int):
    i = lo + 1
    j = hi
    while True:
        while  nums[i] <= nums[lo]:
            if i == hi:
                break
            i += 1
        
        while nums[j] >= nums[lo]:
            if j == lo:
                break
            j -= 1

        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]       
    nums[lo], nums[j] = nums[j], nums[lo]
    return j

if __name__ == "__main__":
    for i in range(40):
        rec.append(randint(0, 10000))
    res = list(rec)

    t0 = time.time()
    quick_sort(rec, 0, 39)
    t1 = time.time()
    print("my_quick_sort runs: %.8f"%(t1-t0))

    t2 = time.time()
    ret = sorted(res)
    t3 = time.time()
    print("Python sorted runs: %.8f"%(t3-t2))