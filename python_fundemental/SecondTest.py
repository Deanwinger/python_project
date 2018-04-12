import unittest
from Second import Node, two_dims_array

class MyAlgoTest(unittest.TestCase):
    def test_prob3(self):
        array = [
            [1, 2, 8, 9],
            [2, 4, 9, 12],
            [4, 7, 10, 13],
            [6, 8, 11, 15],
        ]
        array2 = []
        array3 = [
                    ['a', 'b', 'c'],
                    ['b', 'c', 'd'],
                ]
        array4 = [
                    [62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80],
                    [63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81],
                    [64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82],
                    [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83],
                    [66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84],
                    [67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85],
                ]
        array5 = [
                    [1, 2, 8, 9],
                ]
        array6 = [
                    [1,],
                    [2,],
                    [4,],
                    [6,],
                ]

        self.assertFalse(two_dims_array(array, 5))
        self.assertTrue(two_dims_array(array, 10))
        self.assertTrue(two_dims_array(array, 15))
        self.assertFalse(two_dims_array(array2, 10))
        self.assertTrue(two_dims_array(array3, 'b'))
        self.assertTrue(two_dims_array(array4, 81))
        self.assertFalse(two_dims_array(array5, 7))
        self.assertTrue(two_dims_array(array5, 8))
        self.assertFalse(two_dims_array(array6, 5))
        self.assertTrue(two_dims_array(array6, 6))



if __name__ == "__main__":
    unittest.main()