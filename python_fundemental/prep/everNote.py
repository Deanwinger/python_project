#题1, 把随机序列排序并去重，[1, 3, 4, 2, 3, 4] 
#  转化为 [1, 2, 3, 4]，算出时间以及空间复杂度。

class Solution(object):
    #方法1：Python内置方法
    def unique_and_sort_v0(self, alist):
        res = sorted(set(alist))
        return res

    #方法2, 使用自己实现的快速排序，然后去重
    def unique_and_sort_v1(self):
        pass

    # 待完成， version0 快速排序的经典实现
    def quickSort_v0(self):
        pass
    
    # version1 快速排序的三行实现
    def quickSort_v1(self):
        pass

#题2,version0, 用一行python写出1+2+3+…+10**8 ;
def get_sum():
    sum(range(10**8))

#题2, version1, map, reduce 实现

#题2, version2, 生成器 yield 实现

#题3, 用递归的方式判断字符串是否为回文；
def is_palindrome(string):
    # print(string)
    if len(string) <= 1:
        return True
    
    if string[0] == string[-1]:
        if is_palindrome(string[1:-1]):
            return True
        else:
            return False
    else:
        return False

#题4. 如何遍历一个内部未知的文件夹（两种树的优先遍历方式）
def travel_tree(node):
    pass


if __name__ == "__main__":
    # alist = [1, 3, 4, 2, 3, 4]
    # solu = Solution()
    # print(solu.unique_and_sort_v0(alist))
    a = '123454321'
    b = 'abcba'
    c = '5'
    # print(is_palindrome(a))
    print(is_palindrome(c))