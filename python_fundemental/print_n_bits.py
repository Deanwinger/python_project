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

#自己的程序
class Solution2(object):
    def printNBits(self, n):
        number = ['0']*n
        while not self.Increment(number, n):
            self.printNumber(number, n)
        return 

    def Increment(self, number, length):
        flag= False #判断是否已经是到最后一个数字
        # Inc = False #是否进位

        for i in range(length-1, -1, -1):
            tem = int(number[i]) + 1
            if tem > 9:
                if i == 0:
                    flag = True
                    return flag
                number[i] = str(0)
                # Inc = True
                # if Inc:
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


if __name__ == '__main__':
    # n=1
    # largest = 9999
    # result = []
    # print(numbersByRecursion(n,largest,result))

    # s = Solution()
    # print(s.Print1ToMaxOfNDigits(2))

    s = Solution2()
    print(s.printNBits(4))
