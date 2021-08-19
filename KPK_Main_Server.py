import socket
import threading

Fhost = 'localhost'
Fport = 5000

try:
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((Fhost, Fport))
except:
    print('Error connecting with main server')

host = 'localhost'
port = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()

KPK_PMLN = []
KPK_PTI = []

def RegionThreadStart(conn):
    while True:
        try:
            recv_vote = conn.recv(1024)
            c.send(recv_vote)
            vote = recv_vote.decode()
            if vote == 'PMLN':
                KPK_PMLN.append('vote')
            else:
                KPK_PTI.append('vote')
            
            print('\n')
            print('KPK PMLN votes: ' + str(len(KPK_PMLN)) )
            print('KPK PTI votes: ' + str(len(KPK_PTI)) )
        except:
            conn.close()
            break

print('KPK Server listening')
while True:
    conn, addr = s.accept()
    print('Connected with regional server')
    threading.Thread(target = RegionThreadStart, args= (conn)).start()

    