# leetcode 121. 买卖股票的最佳时机


# 暴力破解, 报超时
class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        
        ret = 0
        for i in range(n):
            for j in range(i, n):
                dif = prices[j]-prices[i]
                if prices[j]>prices[i] and dif >ret:
                    ret = dif
        return ret
        

# pass, 主要是波峰和波谷的考量
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        dif = 0
        bottom = prices[0]
        for i in range(1, n):
            if prices[i] < bottom:
                bottom = prices[i]
            else:
                if prices[i]-bottom > dif:
                    dif = prices[i]-bottom
        return dif


if __name__=='__main__':
    s = [7,1,5,3,6,4]
    solu = Solution2()
    print(solu.maxProfit(s))