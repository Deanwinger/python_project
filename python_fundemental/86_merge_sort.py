from random import randint
import time
# 归并排序

def merge_sort(alist):
    length = len(alist)
    if length <= 1:
        return alist

    mid = length // 2

    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])

    return merge(left, right)

def merge(left, right):
    i = j = 0
    rec = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
             rec.append(left[i])
             i += 1
        else:
            rec.append(right[j])
            j += 1
        
    if i < len(left):
        rec += left[i:]
    if j < len(right):
        rec += left[right:]
        
    return rec


# 8.28 参考普林斯顿算法课程, 不管是快排, 还是此merge sort, 都比python自带的慢一个数量级
def merge(array, aux, lo, mid, hi):
    # 首先复制, 产生一个相同的辅助列表aux, 两指针在这个辅助列表上
    k = lo
    while k<=hi:
        aux[k] = array[k]
        k += 1

    i = k = lo
    j = mid + 1

    while k <= hi:
        if aux[i] <= aux[j]:
            array[k] = aux[i]
            i += 1
        else:
            array[k] = aux[j]
            j += 1
        k += 1
        if i > mid or j > hi:
            break
    
    while i <= mid:
        array[k] = aux[i]
        i += 1
        k += 1

    while j <= hi:
        array[k] = aux[j]
        k += 1
        j += 1
    return 

def msort(alist, aux, lo, hi):
    if hi <= lo:
        return

    mid = (lo + hi) // 2
    msort(alist, aux, lo, mid)
    msort(alist, aux, mid+1, hi)
    merge(alist, aux, lo, mid, hi)
    return 

def merge_s(alist):
    n = len(alist)
    aux = [None]*n
    msort(alist, aux, 0, n-1)


def quick_sort(nums, lo, hi): 
    if lo >= hi:
        return nums
    j = partition(nums, lo, hi)
    quick_sort(nums, lo, j-1)
    quick_sort(nums, j+1, hi)
    return

def partition(nums, lo: int, hi: int):

    i = lo+1
    j = hi
    while True:
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
    nums[lo], nums[j] = nums[j], nums[lo]
    return j

if __name__ == "__main__":
    # a = [1,4,7,6,9,2,5,8]
    # b = list(a)
    # merge_s(a)
    # print(a)

    # print(sorted(b))
    n = 10
    while n:
        ori = rec = []
        for i in range(1000000):
            rec.append(randint(0, 1000000))
        res = list(rec)
        # print("Input rec is: ", rec)
        t0 = time.time()
        merge_s(rec)
        t1 = time.time()
        # print("Sorted rec is: ", rec)
        print("my_merge_s runs: %.8f"%(t1-t0))
        t2 = time.time()
        # quick_sort(res, 0, 999999)
        res = sorted(res)
        t3 = time.time()
        print("my quick_sort runs: %.8f"%(t3-t2))
        # # print("Python sort is: ", ret)
        print("Is my_merge_s return the same value as pythons sorted: ", rec == res)
        if rec != res:
            raise Exception("Whoops, you got it wrong: ", ori)
        n -= 1
        print("="*30)
        
