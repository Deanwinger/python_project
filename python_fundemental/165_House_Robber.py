# leetcode 198. House Robber (Easy)
# leetcode 213. House Robber II (Medium)

'''
leetcode 198
对于第i个房间来说，可以采取抢或不抢。
如果抢的话，截止到当前房间能获得的最大money等于前i-2个房间最大money和当前房间的money。
如果不抢，截止当当前房间能获得的最大money等于前i-1个房间得到的最大money。
public int rob(int[] nums) {
    int pre2 = 0, pre1 = 0;
    for (int i = 0; i < nums.length; i++) {
        int cur = Math.max(pre2 + nums[i], pre1);
        pre2 = pre1;
        pre1 = cur;
    }
    return pre1;
}
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cur = pre2 = pre1 = 0
        for i in range(n):
            cur = max(pre2+nums[i], pre1)
            pre2 = pre1
            pre1 = cur
        return cur


# leetcode 213, 貌似这里只是加了一个限制, 第一个和最后一个相连了, 所以有t1 和 题t2
class Solution:
    def rob(self, nums: List[int]) -> int:
        cur = 0
        if len(nums) <= 1:
            cur = sum(nums)
        else: 
            t1 = nums[1:]
            t2 = nums[:-1]
            cur = max(self.get_money(t1), self.get_money(t2))
        return cur
        
        
    def get_money(self, nums):
        n = len(nums)
        cur = pre2 = pre1 = 0
        for i in range(n):
            cur = max(pre2+nums[i], pre1)
            pre2 = pre1
            pre1 = cur
        return cur