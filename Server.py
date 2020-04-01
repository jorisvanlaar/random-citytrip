"""Joris van laar - Python (PTH) - 20-01-2020"""
import socket
from threading import Thread

connections = []
total_connections = 0


class ClientThread(Thread):
    def __init__(self, socket, address, id, signal):
        Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.signal = signal

    def __repr__(self):
        return f"{self.id} {self.address}"

    def run(self):
        global total_connections
        while self.signal:
            try:
                data = self.socket.recv(32)
            except:
                print(f"ID {self.id}: {str(data.decode('utf-8'))} has logged out")
                self.signal = False
                connections.remove(self)
                total_connections -= 1
                print(f"Total active users: {total_connections}")
                break
            if data != "":
                print(f"ID {self.id}: {str(data.decode('utf-8'))} has logged in")
                print(f"Total active users: {total_connections}")

                """UITGECOMMENT DAT SERVER DE USERNAME VAN DE NIEUW INGELOGDE USER TERUGSTUURT NAAR ALLE CLIENTS"""
                # for client in connections:
                #     client.socket.sendall(data)


def new_connections(socket):
    while True:
        sock, address = socket.accept()
        global total_connections
        connections.append(ClientThread(sock, address, total_connections, True))
        connections[len(connections) - 1].start()
        print(f"New connection at ID {connections[len(connections) - 1]}")
        total_connections += 1


def main():
    host = '127.0.0.1'
    port = 65432

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(3)

    new_connections_thread = Thread(target=new_connections, args=(sock,))
    new_connections_thread.start()


main()

