import socket
import threading

PHost = 'localhost'
PPort = 8000

try:
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((PHost, PPort))
except:
    print('Error connecting with Punjab server')

NRHost = 'localhost'
NRPort = 8001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((NRHost, NRPort))
s.listen()

NR_PMLN = []
NR_PTI = []
Voters = []

def ClientThreadStart(conn,c):
    while True:
        try:
            vote = conn.recv(1024)
            c.send(vote)
            if vote == 'PMLN':
                NR_PMLN.append(vote.decode())
            elif vote == 'PTI':
                NR_PTI.append(vote.decode())
            else:
                'Invalid vote'            
        except:
            conn.close()
            break

print('North region voting begins now')
while True:
    conn, addr = s.accept()
    print('Voter Connected')
    Voters.append(conn)
    threading.Thread(target = ClientThreadStart, args= (conn,c)).start()