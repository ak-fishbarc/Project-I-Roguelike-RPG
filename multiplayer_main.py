import socket
import select
from threading import Thread

""" Multiplayer Client """

def start_client(name: str):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addrs = socket.gethostname()
    port = 12300
    server.connect((addrs, port))
    sockets_list = [socket.socket(), server]

    def response():
        message = sock.recv(2048)
        if message.decode() == 'INVISIBLEREPLYPLACEHOLDERFROMSERVERTOUNBLOCKTHISSOCKETCODE99023':
            pass
        else:
            print(message.decode())

    def write():
        text = input("=>")
        msgs = f'{name}: {text}'
        sock.send(msgs.encode())

    while True:

        read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])
        for sock in read_sockets:
            if sock is server:
                r = Thread(target=response)
                r.start()
                w = Thread(target=write)
                w.start()

