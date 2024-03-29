# leetcode 15. 三数之和

'''
题目描述
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

题目解析
题目需要我们找出三个数且和为 0 ，那么除了三个数全是 0 的情况之外，肯定会有负数和正数，
所以一开始可以先选择一个数，然后再去找另外两个数，这样只要找到两个数且和为第一个选择的
数的相反数就行了。也就是说需要枚举 a 和 b ，将 c 的存入 map 即可。

需要注意的是返回的结果中，不能有有重复的结果。这样的代码时间复杂度是 O(n^2)。
在这里可以先将原数组进行排序，然后再遍历排序后的数组，这样就可以使用双指针以线性时间
复杂度来遍历所有满足题意的两个数组合。
'''