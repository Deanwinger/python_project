from functools import reduce


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
    return sum(range(10**8))

#题2 匿名函数对1~1000求和， version1, map, reduce 实现
def get_sum_v1(alist):
    return reduce(lambda x,y: x+y, alist) if alist else None

#题2, version2, 生成器 yield 实现(实现的很奇怪， 很丑)
def get_sum_v2(alist):
    sums = 0
    def wrapper(alist):
        n = len(alist)
        while n > 0:
            n -= 1
            yield alist[n]
    ret = wrapper(alist)
    for i in ret:
        sums += i
    return sums

#题3, 用递归的方式判断字符串是否为回文；
def is_palindrome(string):
    # print(string)
    if len(string) <= 1:
        return True
    
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False

#题3, 就地检测；
def is_palindrome_v1(string):
    start = 0
    end = len(string)-1
    def wrapper(string, start, end):
        # print(string)
        if start >= end:
            return True
        
        if string[start] == string[end] and start < end:
            start += 1
            end -= 1
            return wrapper(string, start, end)
        else:
            return False
    return wrapper(string, start, end)


#题4. 如何遍历一个内部未知的文件夹（两种树的优先遍历方式）
def travel_tree(node):
    pass


# 题5 求两个数组的差集（例如s1={"a","b","c","d","e"}, s2={"a","e","c"}, 结果应该为{"b","d"}）
def get_single_one(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    return [r for r in s1 if r not in s2] + [r for r in s2 if r not in s1]

# 经典解法   
def get_single_one_v1(s1, s2):
    pass

# 题6 输出k对括号的全部正确匹配方案，如k=2,输出()(),(())
# 卡特兰数问题
# key point：
## 左括号：只要左括号还没有用完， 就可以插入左括号；
## 右括号：只要不造成语法错误， 就可以插入右括号。何时会出现语法错误，如果右括号比左括号多，就会出现语法错误；
# 有问题
def the_parenthese_combination(n):
    strs = [None]*n*2
    alist = []
    addParen(alist, n, n, strs, 0)
    return alist

def addParen(alist, leftRem, rightRem, strs, count):
    if leftRem < 0 or rightRem < leftRem:
        return
    
    if leftRem == 0 and rightRem == 0:
        alist.append(strs)
    else:
        if leftRem > 0:
            strs[count] = '('
            addParen(alist, leftRem-1, rightRem, strs, count + 1)
        if rightRem > leftRem:
            strs[count] = ')'
            addParen(alist, leftRem, rightRem-1, strs, count + 1)
    
# 题6 输出k对括号的全部正确匹配方案，如k=2,输出()(),(())
def the_parenthese_combination_v1(left, right, ret_buf):
    if right < left:
        return
    elif right == 0:
        print(ret_buf)
        return

    if left > 0:
        the_parenthese_combination_v1(left - 1, right, ret_buf + "(")
    if right > 0:
        the_parenthese_combination_v1(left, right - 1, ret_buf + ")")

# 题7 一个字符串表示IP地址，检测是否合法
# leetcode 468


# 题8  n个病人的看病时间，尽量平均的分给m个医生，求每个医生分的时间是多少；
# ZOJ-3334 Body Check


if __name__ == "__main__":
    # alist = [1, 3, 4, 2, 3, 4]
    # solu = Solution()
    # print(solu.unique_and_sort_v0(alist))
    # a = '123454321'
    # b = 'abcba'
    # c = '5'
    # d = 'abcd'
    # print(is_palindrome(a))
    # print(is_palindrome(c))
    # get_sum_v2([1,2,3])
    # print(is_palindrome_v1(a))
    # print(is_palindrome_v1(b))
    # print(is_palindrome_v1(c))
    # print(is_palindrome_v1(d))
    # print(the_parenthese_combination(3))
    the_parenthese_combination_v1(4, 4, "")