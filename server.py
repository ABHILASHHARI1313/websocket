import socket
import threading  # for creating multiple threads

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) # gets the ip address automatically
ADDR = (SERVER,PORT)
print(SERVER)
'''
server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print("[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg = conn.rcv()

def start():
    server.listen()
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

print("[STARTING] server is starting...")
start()

'''