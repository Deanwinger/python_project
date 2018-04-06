"""
    算法第二章，排序
"""


def insertionSort(alist):
    length = len(alist)
    if length <= 1:
        return alist

    for i in range(1, length):
        print(i)
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j-1], alist[j] = alist[j], alist[j-1]
        print(alist)
    return alist

#2.1.6
def shellSort(alist):
    pass

#2.2
def merge_sort(alist):
    length = len(alist)
    if length <= 1:
        return alist

    low = 0
    hi = len(alist)
    mid = hi // 2

    left_list = merge_sort(alist[low:mid])
    right_list = merge_sort(alist[mid:hi])
    return merge(left_list, right_list)

def merge(left_list, right_list):
    if not left_list and not right_list:
        return

    alist = []
    n = len(left_list)
    m = len(right_list)
    i = 0
    j = 0
    while i < n and j < m:
        if left_list[i] <= right_list[j]:
            alist.append(left_list[i])
            i += 1
        else:
            alist.append(right_list[j])
            j += 1

    if i < n:
        alist.extend(left_list[i:])
    
    if j < m:
        alist.extend(right_list[j:])
    return alist



if __name__ == "__main__":
    a = [9,8,4,5,2,6,3,1,7]
    # a = [1,2,3,4,5]
    # print(insertionSort(a))
    # print(merge_sort(a))
    print(merge([3], [1, 7]))