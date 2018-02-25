# import time
# import os
# import sys
# import re

# def testa():
#     print("*"*20)

# def run():
#     n=0
#     print('Run child process %s ...' % (os.getpid()))
#     while n <5:
#         n += 1
#         print("countdown: " + str(n))
#         time.sleep(1)

# def n_factor(x):
#     amount = 1
#     while x > 1:
#         amount = amount * x
#         x -= 1
#     return amount

# #普通版, 使用dict.get()
# def index0():
#     WORD_RE = re.compile(r'\w+')

#     index = {}
#     with open(sys.argv[1], encoding='utf-8') as fp:
#         for line_no, line in enumerate(fp, 1):
#             for match in WORD_RE.finditer(line):
#                 # Match对象上用group()方法提取出子串来, group(0)永远是原始字符串
#                 word = match.group()
#                 col_no = match.start() + 1

#                 location = (line_no, col_no)
#                 occurrences = index.get(word, []) 
#                 occurrences.append(location)
#                 index[word] = occurrences

#     for word in sorted(index, key=str.upper):
#         print(word, index[word])

# #使用setdefault
# def index1():
#     WORD_RE = re.compile(r'\w+')

#     index = {}
#     with open(sys.argv[1], encoding='utf-8') as fp:
#         for line_no, line in enumerate(fp, 1):
#             for match in WORD_RE.finditer(line):
#                 # Match对象上用group()方法提取出子串来, group(0)永远是原始字符串
#                 word = match.group()
#                 col_no = match.start() + 1
#                 location = (line_no, col_no)
#                 index.setdefault(word, []).append(location)

#     for word in sorted(index, key=str.upper):
#         print(word, index[word])




# if __name__ == "__main__":
#     # run()
#     # print(n_factor(8))
#     # index1()
#     pass




import sys, time
import multiprocessing

DELAY = 0.1
DISPLAY = [ '|', '/', '-', '\\' ]

def spinner_func(before='', after=''):
    write, flush = sys.stdout.write, sys.stdout.flush
    pos = -1
    while True:
        pos = (pos + 1) % len(DISPLAY) #此处循环
        msg = before + DISPLAY[pos] + after
        write(msg); flush()
        write('\x08' * len(msg))
        time.sleep(DELAY)

def long_computation():
    # emulate a long computation
    time.sleep(3)

if __name__ == '__main__':
    spinner = multiprocessing.Process(
        None, spinner_func, args=('Please wait ... ', ''))
    spinner.start()
    try:
        long_computation()
        print ('Computation done')
    finally:
        spinner.terminate()