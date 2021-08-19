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
port = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()

P_PMLN = []
P_PTI = []

def RegionThreadStart(conn):
    while True:
        try:
            recv_vote = conn.recv(1024)
            c.send(recv_vote)
            vote = recv_vote.decode()
            if vote == 'PMLN':
                P_PMLN.append('vote')
            else:
                P_PTI.append('vote')
            
            print('\n')
            print('Punjab PMLN votes: ' + str(len(P_PMLN)))
            print('Punjab PTI votes: ' + str(len(P_PTI)))
        except:
            conn.close()
            break

print('Punjab Server listening')
while True:
    conn, addr = s.accept()
    print('Connected with regional server')
    threading.Thread(target = RegionThreadStart, args= (conn)).start()

    