import socket
import logging
import signal
from ./si

HOST = "127.0.0.1"
PORT = 6666

LOGGER = logging.getLogger('Server01')

# Is it right to put it here?
signal.signal(signal.SIGCHLD, sig_chld)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(3) # listen()方法开始监听端口，传入的参数指定等待连接的最大数量
    while True:
        try:
            conn, addr = s.accept()
            str_echo(conn, addr)
        except InterruptedError as err:
            logging.error("Received error %s"%err.errno)
            continue

def str_echo(sock, addr):
    print("Accept connection from %s:%s..."%addr)
    with sock:
        while True:
            data = sock.recv(1024)
            print(data.decode('utf-8'))
            sock.send(data)
            if not data or data.decode("utf-8") == "exit":
                print("==="*20)
                break


if __name__ == "__main__":
    main()