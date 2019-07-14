#  leetcode 209 长度最小的子数组

'''
题目解析
定义两个指针 left 和 right ，分别记录子数组的左右的边界位置。

（1）让 right 向右移，直到子数组和大于等于给定值或者 right 达到数组末尾；
（2）更新最短距离，将 left 像右移一位, sum 减去移去的值；
（3）重复（1）（2）步骤，直到 right 到达末尾，且 left 到达临界位置
'''