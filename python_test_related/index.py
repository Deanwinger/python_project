# 常用test方法
import unittest
from . import create_app
import json


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        # 使用cookie
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    # restful API需要加上这个headers
    def get_api_headers(self):
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def test_captcha(self):
        response = self.client.post('http://127.0.0.1:5000/api/captcha', data=json.dumps({
            'phone': '',
            'country_code': '86'}),
            follow_redirects=True,
            headers=self.get_api_headers())
        print(json.loads(response.data))
        self.assertEqual(response.status_code, 401)