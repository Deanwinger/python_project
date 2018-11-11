import socket
import sys
import time


HOST = '127.0.0.1'    # The remote host
PORT = 6666

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    time.sleep(60)
    s.sendall(sys.argv[1].encode('utf-8'))
    data = s.recv(1024)
    print("Received From Romote Server...\n%s"%str(data.decode("utf-8")))


if __name__ == "__main__":
    main()