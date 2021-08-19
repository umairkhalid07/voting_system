import socket
import pickle
import threading

Fhost = 'localhost'
Fport = 5000

try:
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((Fhost, Fport))
except:
    print('Error connecting with main server')

host = 'localhost'
port = 6000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()

BalochistanPMLN = []
BalochistanPTI = []

def RegionThreadStart(conn):
    while True:
        try:
            recv_vote = conn.recv(1024)
            c.send(recv_vote)
            vote = recv_vote.decode()
            if vote == 'PMLN':
                BalochistanPMLN.append('vote')
            else:
                BalochistanPTI.append('vote')
            
            print('\n')
            print('Balochistan PTI votes: ' + str(len(BalochistanPTI)) )
            print('Balochistan PMLN votes: ' + str(len(BalochistanPMLN)) )
        except:
            conn.close()
            break

print('Balochistan Server listening')
while True:
    conn, addr = s.accept()
    print('Connected with regional server')

    threading.Thread(target = RegionThreadStart, args= (conn)).start()

    