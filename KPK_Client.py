import socket
import threading

host = 'localhost'
port = int(input('Enter 7001 if you are from North KPK or 7002 if you are from South KPK : '))
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((host, port))

while True:
    vote = int(input('Press 1 for PMLN or Press 2 for PTI'))
    if vote == 1 or vote == 2:
        break
    print('Enter valid option')

if vote == 1:
    conn.send('PMLN'.encode())
elif vote == 2:
    conn.send('PTI'.encode())

def recieve(conn):
    while True:
        try:
            votes = conn.recv(1024).decode()
            print('\n')
            print(votes)
        except:
            conn.close()
            break

threading.Thread(target= recieve, args= (conn,) ).start()
