'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

'''
例子：
1  2  8   9
2  4  9   12
4  7  10  13
6  8  11  15
以右上角第一个数（良好的性质， 比下小， 比左大）为参考
'''

# 题3 leetcode 74. Search a 2D Matrix
# leetcode 240. 搜索二维矩阵 II(同此题)
# 2019.2.12

def find_exact_one(matrix, target):
    #情形一：matrix=[]
    if not matrix:
        return False

    #类型判断和数据结构完整性判断
    rows = len(matrix)
    cols = len(matrix[0])

    r_rec = 0
    c_rec = len(matrix[0])-1

    while r_rec < rows and c_rec >= 0:
        if matrix[r_rec][c_rec] == target:
            return True
        elif matrix[r_rec][c_rec] > target:
            c_rec -= 1
        else:
            r_rec += 1
    return False

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        i = 0
        j = cols - 1
        
        while i < rows and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        return False






if __name__ == '__main__':
    array = [
                [1, 2, 8, 9],
                [2, 4, 9, 12],
                [4, 7, 10, 13],
                [6, 8, 11, 15],
            ]
    array2 = []
    array3 = [
                ['a', 'b', 'c'],
                ['b', 'c', 'd'],
            ]
    array4 = [
                [62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80],
                [63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81],
                [64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82],
                [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83],
                [66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84],
                [67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85],
            ]
    array5 = [
                [1, 2, 8, 9],
            ]
    array6 = [
                [1,],
                [2,],
                [4,],
                [6,],
            ]

    # print(find_exact_one(array, 5))
    # print(find_exact_one(array, 10))
    # print(find_exact_one(array, 15))
    # print(find_exact_one(array2, 10))
    # print(find_exact_one(array3, 'b'))
    # print(find_exact_one(array4, 81))
    print(find_exact_one(array5, 8))
    print(find_exact_one(array6, 5))