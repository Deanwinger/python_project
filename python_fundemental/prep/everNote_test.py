import unittest
import everNote

class MyTest(unittest.TestCase):
    def test_pro2_v1(self):
        get_sum = everNote.get_sum_v1
        alist = list(range(1000))
        self.assertEqual(sum(alist), get_sum(alist))

    def test_pro2_v2(self):
        get_sum = everNote.get_sum_v2
        alist = list(range(1000))
        # print("="*40, list(get_sum(alist)))
        self.assertEqual(sum(alist), get_sum(alist))
        
    def test_pro5_v1(self):
        get_single_one = everNote.get_single_one
        s1 = 'abcde'
        s2 = 'aec'
        self.assertEqual(['b', 'd'], get_single_one(s1, s2))





if __name__ == "__main__":
    unittest.main()
