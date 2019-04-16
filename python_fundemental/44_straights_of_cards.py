'''
随机从扑克牌中抽出了5张牌,判断是不是顺子,
决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
'''

# 题44 这题其实算是业务抽象了, 一系列规则
class Solution:
    def IsContinuous(self, numbers):
        # 边界条件
        if not numbers:
            return False
        
        if len(numbers) < 5:
            return False

        n = len(numbers)
        # 先排序, 最重要的一步
        numbers = sorted(numbers)
        
        num_of_zero = 0
        num_of_gap = 0
        
        # 统计0的个数
        for num in numbers:
            if num == 0:
                num_of_zero += 1
                
        # 统计间隔数
        sml = 0
        big = 1
        while big < n:
            # 由于0是可变的, 所以需要先排除掉, 如果拿到的有对子, 直接return False
            if numbers[sml] != 0 and numbers[big]!=0 and numbers[sml] == numbers[big]:
                return False
            # 需要把0 排除在比较之外
            if numbers[sml] !=0 and numbers[big]-numbers[sml]!=1:
                num_of_gap += numbers[big]-numbers[sml]-1
                if num_of_gap > num_of_zero:
                    return False
            sml = big
            big += 1
        return num_of_zero >= num_of_gap
        


if __name__ == "__main__":
    s = Solution()
    a = [1,3,2,5,4]
    print(s.IsContinuous(a))