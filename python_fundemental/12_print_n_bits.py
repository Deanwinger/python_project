'''
输入数字n, 按顺序打印从1最大的n位十进制数
比如输入3, 则打印出1、2、3、到最大的3位数即999
'''

# 题12

#此方法最多只能打印到996， 超过即会报 RecursionError: maximum recursion depth exceeded in comparison
def numbersByRecursion(n,largest,result):
    def recursion(num,largest,result):
        if num <= largest:
            result.append(num)
            return recursion(num+1,largest,result) 
        else:
            return result
    return recursion(n,largest,result)

# 9.2 因为没有最大数的限制, 生成器毫无疑问是最优解
def numsOfNBits(largest):
    num = 0
    while num < largest:
        num += 1
        yield num


#参考： 转换成字符串来输出
#举例n=3， number=[0,0,0]开始, 在原number数组上直接修改 
class Solution(object):
    def Print1ToMaxOfNDigits(self, n):
        if n <= 0:
            return

        number = ['0'] * n
        while not self.Increment(number):
            print('*'*10, number, '*'*10)
            self.PrintNumber(number)

    def Increment(self, number):
        isOverflow = False
        nTakeOver = 0
        nLength = len(number)

        for i in range(nLength-1, -1, -1):
            nSum = int(number[i]) + nTakeOver
            if i == nLength - 1:
                nSum += 1

            if nSum >= 10:
                if i == 0:
                    isOverflow = True
                else:
                    nSum -= 10
                    nTakeOver = 1
                    number[i] = str(nSum)
            else:
                number[i] = str(nSum)
                break

        return isOverflow

    def PrintNumber(self, number):
        isBeginning0 = True
        nLength = len(number)

        for i in range(nLength):
            if isBeginning0 and number[i] != '0':
                isBeginning0 = False
            if not isBeginning0:
                print('%c' % number[i], end='')
        print('')

# 反复研究
# 自己的程序
class Solution2(object):
    def printNBits(self, n):
        number = ['0']*n
        while not self.Increment(number, n):
            self.printNumber(number, n)
        return 

    def Increment(self, number, length):
        flag= False #判断是否已经是到最后一个数字

        for i in range(length-1, -1, -1):
            tem = int(number[i]) + 1
            if tem > 9:
                if i == 0:
                    flag = True
                    return flag
                number[i] = str(0)
                continue
            else:
                number[i] = str(tem)
                break
        return flag

    def printNumber(self, number, length):
        for i in range(length):
            if number[i] != '0':
                tem = number[i:]
                break
        s = ''
        for i in tem:
            s += i
        print(s)

# 9.3 此题用全排列更合适
class Solu:
    def P1ToMaxOfNDigits(self, n):
        nums = ['0'] * n
        largest = ['9'] * n
        while True:
            self.increment(nums, n)
            # print("="*20, nums)
            self.print_num(nums, n)
            if nums == largest:
                return 

            
    def increment(self, nums, length):
        take_over = 0
        for i in range(length-1, -1, -1):
            cur = int(nums[i]) + 1
            if cur >= 10:
                nums[i] = str(cur - 10)
                take_over = 1
            else:
                nums[i] = str(cur)
                take_over = 0

            if take_over == 0:
                break
    
    def print_num(self, nums, n):
        zero_start = True
        for i in range(n):
            if nums[i] == '0' and zero_start == True:
                continue
            else:
                zero_start = False
                print(nums[i], end='')
        print('')































if __name__ == '__main__':
    # n=1
    # largest = 9999
    # result = []
    # print(numbersByRecursion(n,largest,result))

    # s = Solution()
    # print(s.Print1ToMaxOfNDigits(2))

    s = Solu()
    print(s.P1ToMaxOfNDigits(4))
    # a = numsOfNBits(9999)
    # for i in a:
    #     print(i)
