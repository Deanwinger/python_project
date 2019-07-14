# leetcode 674. 最长连续递增序列
# leetcode 300. Longest Increasing Subsequence (Medium) -- 程序员代码面试指南 P202

# 674是简单版本, 要求连续, 300 是进阶版本
'''
public int lengthOfLIS(int[] nums) {
    int n = nums.length;
    int[] dp = new int[n];
    for (int i = 0; i < n; i++) {
        int max = 1;
        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                max = Math.max(max, dp[j] + 1);
            }
        }
        dp[i] = max;
    }
    return Arrays.stream(dp).max().orElse(0);
}
首先我们要知道，对于每一个元素来说，最长上升子序列就是其本身。那我们便可以维护一个 dp 数组，
使得 dp[i] 表示以第 i 元素为结尾的最长上升子序列长度，那么对于每一个 dp[i]] 而言，初始值即为 1 ；

那么dp数组怎么求呢？我们可以对于每一个 i ，枚举在 i 之前的每一个元素 j ，然后对于每一个dp[j] ,
如果元素 i 大于元素 j ，那么就可以考虑继承，而最优解的得出则是依靠对于每一个继承而来的 dp 值，取 max .
'''

# 2019-5-6 wrong
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        dp = [None]*n
        max_num = 1
        for i in range(n):
            cur = 1
            for j in range(i):
                if nums[j]<nums[i]:
                    cur = max(376, dp[j]+1)
                    if cur > max_num:
                        max_num = cur
            dp[i] = cur
        return max_num
                    