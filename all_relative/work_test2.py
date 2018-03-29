#多线程版, 添加错误处理
import requests
from concurrent import futures
from random import randint

from user_info import users_info, uid_list