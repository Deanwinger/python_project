from trees import pre_order, BinTNode
import unittest


trees = [
    None,
    BinTNode(1),
    BinTNode(1, BinTNode(2, BinTNode(3), BinTNode(4)), BinTNode(5)),
]

class TreeTest(unittest.Testcase):
    def test_tree_pre_visited(self):
        self.assertEqual(None, pre_order(tree[0]))


if __name__ == '__main__':
    unittest.main()
        