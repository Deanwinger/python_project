import unittest
from insertSort213 import insertionSort, merge_sort
import random



def create_random_list():
    return [random.randint(0,10000000) for _ in range(200000)]
    

class MyTest(unittest.TestCase):
    # def test_insertion_sort(self):
    #     for i in lists:
    #         self.assertEqual(sorted(i), insertionSort(i))

    def test_merge_sort(self):
        for i in lists:
            self.assertEqual(sorted(i), merge_sort(i))

if __name__ == "__main__":
    ran_list = create_random_list()

    lists = [
        [],
        [1],
        [1,2,3,4,5],
        [6,5,4,3,2,1],
        [9,8,4,5,2,6,3,1,7],
        ran_list,
    ]
    unittest.main()