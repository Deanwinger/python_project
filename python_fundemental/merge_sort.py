
# def mergeSort(alist):
#     if not alist or alist is None:
#         return
#     else:
#         mid = len(alist) // 2
#         left_half = alist[:mid]
#         right_half = alist[mid:]

#         mergeSort

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0; j = 0; k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
            print('step one: %s' % alist)

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
        print('step two: %s' % alist)




if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    mergeSort(alist)
    print(alist)