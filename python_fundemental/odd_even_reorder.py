'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''
#题14
# leetcode 328. Odd Even Linked List, 使用的是linked_list

class Solution(object):
    def reorder_odd_even(self, array):
        if len(array) <= 1:
            return
        j = len(array) - 1
        for i in range(len(array)):
            if self.is_even(array[i]):
                #偶数， 则开始判断尾部
                while self.is_even(array[j]):
                    j -= 1
                if i >= j:
                    return array
                else:
                    array[i], array[j] = array[j], array[i]
        return

    def is_even(self, n):
        return n % 2 == 0


if __name__=='__main__':
    array1 = [1,2,3,4,5]
    array2 = [1,3,5,7,2,4]
    array3 = [2,4,6,1,3,5]
    array4 = [-1, 2, -3, 4, -10, -5, -6, 7, 8, 9, 10]
    s = Solution()
    # print(s.find_recursively(array, i=0, j=len(array)-1))
    print(s.reorder_odd_even(array1))
    print(s.reorder_odd_even(array2))
    print(s.reorder_odd_even(array3))
    print(s.reorder_odd_even(array4))