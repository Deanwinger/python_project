from threading import Thread, Event
import time

def countDown(n, start_evt):
    print('countdown starting')
    start_evt.set()
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(5)


if __name__=='__main__': 
    start_evt = Event()
    print('Launching countdown')
    t = Thread(target=countDown, args=(10, start_evt))
    t.start()
    start_evt.wait()
    print('countdown is running')
