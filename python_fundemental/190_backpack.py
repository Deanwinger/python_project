# 0_1 背包问题

'''

有一个容量为 N 的背包，要用这个背包装下物品的价值最大，这些物品有两个属性：体积 w 和价值 v。

定义一个二维数组 dp 存储最大价值，其中 dp[i][j] 表示前 i 件物品体积不超过 j 的情况下能达到
的最大价值。设第 i 件物品体积为 w，价值为 v，根据第 i 件物品是否添加到背包中，可以分两种情
况讨论：

第 i 件物品没添加到背包，总体积不超过 j 的前 i 件物品的最大价值就是总体积不超过 j 的前 i-1 
件物品的最大价值，dp[i][j] = dp[i-1][j]。
第 i 件物品添加到背包中，dp[i][j] = dp[i-1][j-w] + v。

public int knapsack(int W, int N, int[] weights, int[] values) {
    int[][] dp = new int[N + 1][W + 1];
    for (int i = 1; i <= N; i++) {
        int w = weights[i - 1], v = values[i - 1];
        for (int j = 1; j <= W; j++) {
            if (j >= w) {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - w] + v);
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }
    return dp[N][W];
}
'''

def backpack(cap, values, weights):
    '''
    cap: the capacity of a bag, 对应列
    v: lists, item values
    w: lists, contains single item weight
    '''
    # if len(v) != len(w):
    #     return
    n = len(values) #对应行
    dp = [[0]*(cap+1) for _ in range(n+1)]
    for i in range(1,n+1):
        w = weights[i-1]
        v = values[i-1]
        for j in range(1, cap+1):
            if j >= w:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)
    return dp[n][cap]


'''
空间优化
'''
def backpack_v1(cap, values, weights):
    pass


if __name__=='__main__':
    vs = [6,10,12]
    ws = [1,2,3]
    cap = 5
    print(backpack(cap, vs, ws))
