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
        return nums
    j = partition(nums, lo, hi)
    quick_sort(nums, lo, j-1)
    quick_sort(nums, j+1, hi)
    return nums

def partition(nums, lo: int, hi: int):
    # print("pivot is: %d"%nums[lo])
    # print("lo is: %d"%lo)
    # print("hi is: %d"%hi)
    # print("Cur nums: ", nums)
    i = lo
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
        # print("temp nums is: ", nums)       
    nums[lo], nums[j] = nums[j], nums[lo]
    # print("Current nums is: ", nums)
    # print("j is: ", j)
    # print("="*30)
    return j

# Python cookbook的算法, 非常直观
def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        return qsort([x for x in arr[1:] if x < pivot]) + \
               [pivot] + \
               qsort([x for x in arr[1:] if x >= pivot])

#### 快速排序的另一种实现
def quick_sort1(lst):
   def qsort(lst, begin, end):
       if begin >= end:
           return
       pivot = lst[begin]
       i = begin
       for j in range(begin + 1, end + 1):
           if lst[j] < pivot: # 发现一个小元素
               i += 1
               lst[i], lst[j] = lst[j], lst[i] # 小元素交换到前面
       lst[begin], lst[i] = lst[i], lst[begin] # 枢轴元素就位
       qsort(lst, begin, i - 1)
       qsort(lst, i + 1, end)

   qsort(lst, 0, len(lst) - 1)

if __name__ == "__main__":
    a = [36, 42, 33]
    b = [5, 4]
    print("Input rec is: ", a)
    hi = len(a) - 1
    print(quick_sort(a, 0, hi))

    # rec = []
    # for i in range(100000):
    #     rec.append(randint(0, 100000))
    # res = list(rec)
    # print("Input rec is: ", rec)
    # t0 = time.time()
    # quick_sort(rec, 0, 99999)
    # t1 = time.time()
    # print("Sorted rec is: ", rec)
    # print("my_quick_sort runs: %.8f"%(t1-t0))
    # t2 = time.time()
    # ret = sorted(res)
    # t3 = time.time()
    # print("Python sorted runs: %.8f"%(t3-t2))
    # # print("Python sort is: ", ret)
    # print("Is my_quick_sort return the same value as pythons sorted: ", rec == ret)

    # t4 = time.time()
    # t = quick_sort1(res)
    # t5 = time.time()
    # print("Total time is: %.8f"%(t5-t4))