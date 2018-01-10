import time, os

def run():
    n=0
    print('Run child process %s ...' % (os.getpid()))
    while n <5:
        n += 1
        print("countdown: " + str(n))
        time.sleep(1)

def n_factor(x):
    amount = 1
    while x > 1:
        amount = amount * x
        x -= 1
    return amount

if __name__ == "__main__":
    # run()
    print(n_factor(8))

