import socket
import threading

SHost = 'localhost'
SPort = 8000

try:
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((SHost, SPort))
except:
    print('Error connecting with Punjab server')

SRHost = 'localhost'
SRPort = 8002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRHost, SRPort))
s.listen()
SR_PMLN = []
SR_PTI = []
Voters = []

def ClientThreadStart(conn,c ):
    while True:
        try:
            vote = conn.recv(2048)
            c.send(vote)
            if vote == 'PMLN':
                SR_PMLN.append(vote.decode())
            elif vote == 'PTI':
                SR_PTI.append(vote.decode())
            else:
                'Invalid Vote'
                
        except:
            conn.close()
            Voters.remove(conn)
            break

print('South region voting begins now')
while True:
    conn, addr = s.accept()
    print('Voter Connected')
    Voters.append(conn)
    threading.Thread(target = ClientThreadStart, args= (conn,c)).start()