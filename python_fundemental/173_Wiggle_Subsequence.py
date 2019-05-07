# leetcode 376. Wiggle Subsequence (Medium)

'''
public int wiggleMaxLength(int[] nums) {
    if (nums == null || nums.length == 0) {
        return 0;
    }
    int up = 1, down = 1;
    for (int i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i - 1]) {
            up = down + 1;
        } else if (nums[i] < nums[i - 1]) {
            down = up + 1;
        }
    }
    return Math.max(up, down);
}

'''

# 2019-5-7 有问题, Corner case [0,0,0],需要考虑, 硬编码的方式很丑
class Solution:
    def wiggleMaxLength(self, nums) -> int:
        n = len(nums)
        if n <= 1:
            return n

        if n == 2 and nums[0] == nums[1]:
            return 1
        else:
            t = []
            for i in range(1, n):
                # print("dp is:", dp)
                print("t is:", t)
                # print("max is: ", max)
                # print("=="*3)
                tem = nums[i] - nums[i-1]
                t.append(tem)

            cur = 1
            # [16, -12, 5, 3, 2, -5, -5, 11, -8]
            for i in range(1, len(t)):
                if self.is_opposites(t[i], t[i-1]):
                    cur += 1
            return cur + 1
        
    def is_opposites(self, x, y):
        return (x>0 and y<0) or (x<0 and y>0)


if __name__=='__main__':
    s = Solution()
    a = [1,17,5,10,13,15,10,5,16,8]
    print(s.wiggleMaxLength(a))
    