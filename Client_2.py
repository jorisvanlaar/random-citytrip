"""Joris van laar - Python (PTH) - 20-01-2020"""
import sys
import socket
from threading import Thread
import App


def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(32)
            print(str(data.decode("utf-8")))
        except:
            print('You have logged out')
            break


host = '127.0.0.1'
port = 65432

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
except:
    print("Could not make a connection to the server")
    input("Press ENTER to quit")
    sys.exit(0)

receive_thread = Thread(target=receive, args=(sock, True))
receive_thread.start()

print("What is your username?")
username = input()
sock.sendall(str.encode(username))

App.logo()
App.greeting()
App.menu()

sock.close()
