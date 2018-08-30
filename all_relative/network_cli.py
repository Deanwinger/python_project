"""
使用concurrent future 来模拟并发
"""

from socket import socket


def send_message():
    s = socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 8888))

    s.send("hello Alan, how are you doing")
    buffer = []
    while True:
        data = s.recv(1024)
        if data:
            buffer.append(data)
        else:
            break
    print("buffer is: ", buffer)


if __name__ == "__main__":
    send_message()