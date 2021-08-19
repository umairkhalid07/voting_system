import socket
import threading

host = 'localhost'
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()

PMLN = []
PTI = []
Provinces = []

def ProvinceThreadStart(conn):
    while True:
        try:
            vote = conn.recv(1024).decode()
            if vote == 'PMLN':
                PMLN.append('vote')
            else:
                PTI.append('vote')

            print('\n')
            print('PMLN votes: ' + str(len(PMLN)) )
            print('PTI votes: ' + str(len(PTI)) )
            
        except:
            conn.close()
            Provinces.remove(conn)
            break


print('Main Server listening')
while True:
    conn, addr = s.accept()
    print('Connected with provincial server')
    Provinces.append(conn)
    threading.Thread(target = ProvinceThreadStart, args= (conn, addr)).start()