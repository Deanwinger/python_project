import unittest

from word_match import check_user_input

class MyTests(unittest.TestCase):
    def test_user_input(self):
        self.assertTrue(check_user_input("helloworld"))
        self.assertTrue(check_user_input("技术部高级后台开发"))
        self.assertTrue(check_user_input("高级运营总监"))
        
        self.assertRaises(Exception, check_user_input, "       ")
        self.assertRaises(Exception, check_user_input, "大")
        self.assertRaises(Exception, check_user_input, "大中华区华南高级区域代表兼华南区总裁助理")
        self.assertRaises(Exception, check_user_input, "_市场研究员")
        self.assertRaises(Exception, check_user_input, "产品经理+++")

if __name__ == "__main__":
    unittest.main()

        

