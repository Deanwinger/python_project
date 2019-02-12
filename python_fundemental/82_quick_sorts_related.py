# 快速排序

from random import randint
import time 



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

"""
    basic plan:
        1. Shuffle the array -- 可用random.shuffle, 就地打乱,random.shuffle 
           函数不关心参数的类型,只要那个对象实现了部分可变序列协议即可
        2. partition 函数返回j才是正确的, 如果返回i, 就出错, 为什么

        3. sort
"""

def quick_sort(nums, lo, hi): 
    if lo >= hi:
        return 
    j = partition(nums, lo, hi)
    quick_sort(nums, lo, j-1)
    quick_sort(nums, j+1, hi)
    return 

def partition(nums, lo: int, hi: int):
    # print("current lo is: ", lo)
    # print("current hi is: ", hi)
    # print("current pivot is: ", nums[lo])
    # print("current nums is: ", nums)
    i = lo+1
    j = hi
    # n = 20
    while True:
    # while i < j:
        while  nums[i] < nums[lo]:
            if i == hi:
                break
            i += 1

        while nums[j] > nums[lo]:
            if j == lo:
                break
            j -= 1
        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
        # print("temp nums is: ", nums)
        # n -= 1
    nums[lo], nums[j] = nums[j], nums[lo]
    # print("The nums is: ", nums)
    # print("The current j is: ", j)
    # print("="*30)
    return j


if __name__ == "__main__":
    # 此例可用于研究为什么不能用i, to be finished
    a = [8, 2, 3, 1, 6, 3, 5, 9, 9, 10]
    print("Input rec is: ", a)
    hi = len(a) - 1
    print(quick_sort(a, 0, hi))
    print(a)


    # n = 10
    # while n:
    #     ori = rec = []
    #     for i in range(10):
    #         rec.append(randint(0, 20))
    #     res = list(rec)
    #     # print("Input rec is: ", rec)
    #     t0 = time.time()
    #     quick_sort(rec, 0, 9)
    #     t1 = time.time()
    #     # print("Sorted rec is: ", rec)
    #     print("my_quick_sort runs: %.8f"%(t1-t0))
    #     t2 = time.time()
    #     ret = sorted(res)
    #     t3 = time.time()
    #     print("Python sorted runs: %.8f"%(t3-t2))
    #     # print("Python sort is: ", ret)
    #     print("Is my_quick_sort return the same value as pythons sorted: ", rec == ret)
    #     if rec != ret:
    #         raise Exception("Whoops, you got it wrong: ", ori)
    #     n -= 1
    #     print("="*30)
        

    # t4 = time.time()
    # t = quick_sort1(res)
    # t5 = time.time()
    # print("Total time is: %.8f"%(t5-t4))