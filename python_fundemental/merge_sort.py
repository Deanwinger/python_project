def mergeSort(alist):
    print("alist---%s"%alist)
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    left = mergeSort(alist[:mid])
    right = mergeSort(alist[mid:])
    print("left---%s"%left)
    print("right---%s"%right)
    return merge(left, right)

def merge(left, right):
    temp = []
    i=j=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
    
    while i < len(left):
        temp += left[i:]
        i += 1
    
    while j < len(right):
        temp += right[j:]
        j += 1
    print("merge--%s"%temp)
    return temp



if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    a = mergeSort(alist)
    print(a)