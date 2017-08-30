import socket
from cryptography.fernet import Fernet

HOST = '127.0.0.1'    # The remote host
PORT = 1337           # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
key = s.recv(1024)
cipher_suite = Fernet(key)
while True:
	cmd=raw_input('#')
	cmde=cipher_suite.encrypt(cmd)
	s.sendall(cmde)
	data = s.recv(1024)
	datadec=cipher_suite.decrypt(data)
	print datadec
s.close()
