import socket
import _thread

""" Multiplayer Server """


def start_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    addrs = socket.gethostname()
    port = 12300
    server.bind((addrs, port))
    server.listen(5)
    list_of_clients = []

    def clientthread(conn, addr):
        conn.send(b'INVISIBLEREPLYPLACEHOLDERFROMSERVERTOUNBLOCKTHISSOCKETCODE99023')
        while True:
            try:
                message = conn.recv(2048)
                if message:
                    #print('<' + addr[0] + '> ' + message.decode())
                    message_to_send = message.decode()
                    broadcast(message_to_send, conn)
                    conn.send(message_to_send.encode())
                else:
                    remove(conn)
            except:
                continue

    def broadcast(message, connection):
        for clients in list_of_clients:
            if clients != connection:
                try:
                    clients.send(message.encode())
                except:
                    clients.close()
                    remove(clients)

    def remove(connection):
        if connection in list_of_clients:
            list_of_clients.remove(connection)

    while True:

        conn, addr = server.accept()
        list_of_clients.append(conn)
        print(addr[0] + ' connected')
        _thread.start_new_thread(clientthread, (conn, addr))

