import unittest
from Second import Node, two_dims_array, rm_llist_node
from everNote import is_palindrome

class MyAlgoTest(unittest.TestCase):
    # def test_prob3(self):
    #     array = [
    #         [1, 2, 8, 9],
    #         [2, 4, 9, 12],
    #         [4, 7, 10, 13],
    #         [6, 8, 11, 15],
    #     ]
    #     array2 = []
    #     array3 = [
    #                 ['a', 'b', 'c'],
    #                 ['b', 'c', 'd'],
    #             ]
    #     array4 = [
    #                 [62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80],
    #                 [63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81],
    #                 [64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82],
    #                 [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83],
    #                 [66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84],
    #                 [67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85],
    #             ]
    #     array5 = [
    #                 [1, 2, 8, 9],
    #             ]
    #     array6 = [
    #                 [1,],
    #                 [2,],
    #                 [4,],
    #                 [6,],
    #             ]

    #     self.assertFalse(two_dims_array(array, 5))
    #     self.assertTrue(two_dims_array(array, 10))
    #     self.assertTrue(two_dims_array(array, 15))
    #     self.assertFalse(two_dims_array(array2, 10))
    #     self.assertTrue(two_dims_array(array3, 'b'))
    #     self.assertTrue(two_dims_array(array4, 81))
    #     self.assertFalse(two_dims_array(array5, 7))
    #     self.assertTrue(two_dims_array(array5, 8))
    #     self.assertFalse(two_dims_array(array6, 5))
    #     self.assertTrue(two_dims_array(array6, 6))

    # def test_prob13(self):
    #     for i in range(10):
    #         llist = self.construct_llist()
    #         # self.llist_trave(llist[0])
    #         rm_llist_node(llist[0], llist[i])
    #         self.llist_trave(llist[0])

    # def construct_llist(self):
    #     rec = [Node(i) for i in range(10, 20)]
    #     for i in range(10):
    #         if i == 9:
    #             rec[i].next = None
    #         else:
    #             rec[i].next = rec[i+1]
    #     return rec

    # def llist_trave(self, root):
    #     while root:
    #         print(root.val)
    #         root = root.next
    #     print("="*20)

    def test_is_palindrome(self):
        rec0 = [
            '',
            ' ', #1空格
            '  ', #两空格
            'a',
            '123454321',
            'abcba'
        ]
        rec1 = [
            'abc',
            ' abcba'
        ]
        for i in rec0:
            self.assertTrue(is_palindrome(i))
        for j in rec1:
            self.assertFalse(is_palindrome(j))

if __name__ == "__main__":
    unittest.main()