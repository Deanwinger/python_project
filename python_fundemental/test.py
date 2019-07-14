from random import randint
from faker import Faker
from collections import namedtuple

# class Testcases:
#     def __init__(self, m):
#         self.elem = m

#     def find_self(self):
#         """This is a class made for test"""
#         return self.elem



class Solution:
    def majorityElement(self, nums) -> int:
        n = len(nums)
        if not n:
            return 
        if n== 1:
            return nums[0]
        
        mid = n//2
        start = 0
        end = n-1
        index = self.partition(nums, start, end)
        while index != mid:
            if index < mid:
                start = index+1 
                index = self.partition(nums, start, end)
            else:
                end = index - 1
                index = self.partition(nums, start, end)
        return nums[index]
            
    def partition(self, nums, lo, hi):
        i = lo+1
        j = hi

        pivot = lo
        while True:
            while nums[i] < nums[pivot]:
                if i == hi:
                    break
                i += 1

            while nums[j] > nums[pivot]:
                if j == lo:
                    break
                j -= 1

            if i>=j:
                break
            else:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        nums[lo], nums[j] = nums[j], nums[lo]
        return j


def main():
    with open('temp.txt', 'r') as fp:
        t = fp.read()
        print(type(t))
        print(t)

class A:
    def __init__(self, x):
        self.x = x

    def __call__(self, y):
        return self.x+y

Result = namedtuple('Result', 'count average')

# 子生成器
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)

# 委派生成器
def grouper(results, key):
    # while True:
    #     results[key] = yield from averager()
    results[key] = yield from averager()
    print(results)    
    # return 'For test'


# 客户端代码,即调用方
def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        # try:
        # print(results)
        group.send(None) # 重要!
        # except StopIteration as exc:
        #     print("The return value is: ", exc.value)
    # print(results)
    report(results)
    # 如果要调试,去掉注释
    # 输出报告

def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))





if __name__ == '__main__':
    # s = [8,8,7,7,7]
    # sol = Solution()
    # print(sol.majorityElement(s))
    # main()
    # a = A(1)
    # print(a(2))
    data = {
        'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
        'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
        'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
        'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
    }
    main(data)