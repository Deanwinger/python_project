from random import randint
from faker import Faker

fake = Faker(locale='zh_CN')

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def fake_file():
    n = 10000
    with open("test.txt", 'w', encoding='utf-8') as fp:
        while n > 0:
            fp.write("{} {}\n".format(fake.name(), randint(0, 100)))
            n -= 1

def sort_by_name():
    with open("test.txt", 'r') as fp:
        rec = []
        content = fp.readlines()
        for c in content:
            remain = c.split()
            rec.append(remain)
        res = sorted(rec, key=lambda x: int(x[-1]))

    with open("test_after_sort", 'w', encoding="utf-8") as fp:
        for r in res:
            s = ''
            for item in r:
                s = s + ' ' + str(item)
            s += '\n'
            fp.write(s)

def high_func():
    rec = []
    for i in range(5):
        rec.append(lambda x: x*i)
    
    for r in rec:
        print("current r is: ",r(2))

def test():
    flist = []
    for i in range(3):
        def afunc(x, i=i):
            return x*i
        flist.append(afunc)

    print("flist is: ", flist)
    for f in flist:
        print(f(2))


def count_print(N):
    return 2**(N-1)
if __name__ == '__main__':
    print(count_print(6))
