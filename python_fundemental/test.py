import time, os

def run():
    n=0
    print('Run child process %s ...' % (os.getpid()))
    while n <5:
        n += 1
        print("countdown: " + str(n))
        time.sleep(1)


if __name__ == "__main__":
    run()