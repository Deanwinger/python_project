from functools import reduce

# 题目1~21

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
# Pv4 地址由十进制数和点来表示，每个地址包含4个十进制数，其范围为 0 - 255， 用(".")分割。比如，172.16.254.1；同时，IPv4 地址内的数不会以 0 开头。比如，地址 172.16.254.01 是不合法的。
# IPv6 地址由8组16进制的数字来表示，每组表示 16 比特。这些组数字通过 (":")分割。比如,  2001:0db8:85a3:0000:0000:8a2e:0370:7334 是一个有效的地址。而且，我们可以加入一些以 0 开头的数字，字母可以使用大写，也可以是小写。所以， 2001:db8:85a3:0:0:8A2E:0370:7334 也是一个有效的 IPv6 address地址 (即，忽略 0 开头，忽略大小写)
class IPValidation:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        def IP4(s):
            if s.count('.')!=3:
                return False
            items = s.split('.')
            for item in items:
                if not item4(item):
                    return False
            return True
        def IP6(s):
            if s.count(':')!=7:
                return False
            items = s.split(':')
            for item in items:
                if not item6(item):
                    return False
            return True
        
        def item4(item):
            if not item:
                return False
            if item[0]=='0' and item!='0':
                return False
            for c in item:
                if (not c>='0') or (not c<='9'):
                    return False
            return 0<=int(item)<=255
            
        def item6(item):
            if not item or len(item)>4:
                return False
            item = item.lower()
            for c in item:
                if (not c>='0' or not c<='9') and (not c>='a' or not c<='f'):
                    return False
            return True
            
        
        if IP.find('.')!=-1:
            return 'IPv4' if IP4(IP) else 'Neither'
        elif IP.find(':')!=-1:
            return 'IPv6' if IP6(IP) else 'Neither'
        return 'Neither'


# 题8  n个病人的看病时间，尽量平均的分给m个医生，求每个医生分的时间是多少；
# ZOJ-3334 Body Check


# 题9 一个列表A=[A1，A2，…,An]，要求把列表中所有的组合情况打印出来
# 适合醒瞌睡
# 两种情况， 1、没有重复的， 2、有重复的
def combination(alist):
    if not alist:
        return []
    
    if len(alist) == 1:
        return list(alist)

    rec = []
    for i in range(len(alist)):
        # print(alist[i]
        # rec.append(list(alist[i]))
        temp = combination(alist[:i] + alist[i+1:])
        rec.append(list(alist[i]) + temp)
    print(rec)
    return rec    
    

# 题9， 字符串的排列, 写的稀糟的
def permutation(strings):
    """固定第一个，然后递归"""
    n = len(strings)
    if n <= 1:
        return strings

    rec = []
    for i in range(n):
        # print("*"*10,i)
        s = ''.join(strings[:i]) + ''.join(strings[i+1:])
        # print(s)
        # print("="*20, s, "="*20, strings[i])
        temp = strings[i] + permutation(s)
        rec.append(temp)
        print(rec)
        # print(temp)
    return temp

# 题10 一个长度n的无序数字元素列表，如何求中位数，如何尽快的估算中位数，你的算法复杂度是多少；
# 方法一： 用堆来实现
# 方法二： 利用快排的思想 
# 1、先进行一趟快排，使得div左边的值都比arr[div]小，div右边的值都比arr[div]大，但是这个div的位置是不确定的，可能位于中间，也可能偏左或者偏右。 
# 2、计算出mid所在的下标，如果是奇数则是mid=(size+1)/2，如果是偶数则是mid=size/2。 
# 3、此时需要比较mid和div所在的位置。如果mid在div所在位置的左边，此时就要递归去左半区间查找；如果mid在div的右边，此时就要递归去右半区间查找；如果恰好相等则说明div/mid所在的位置就是中位数。 
# 代码实现如下

# 题11
# 约瑟夫环

# 题12
# 单向链表长度未知，如何判断其中是否有环；
# 141. Linked List Cycle
def has_circle(Node):
    if head is None or head.next is None:
        return False
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    return False




# =====================================================================================================

# 题13
# 接上题，找到环的入口点
# leetcode 142. Linked List Cycle II

# 题14
# 判断两个链表是否相交

# 题15
# 单链表逆置

# =====================================================================================================

# 题目16

# 题目17

# 题目18

# =====================================================================================================

# 题目19
# 题目20
# 题目21
# =====================================================================================================


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
    # the_parenthese_combination_v1(4, 4, "")
    strings = 'abc'
    alist = ['a', 'b', 'c']
    # permutation(strings)
    combination(alist)