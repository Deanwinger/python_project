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
    res = []
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