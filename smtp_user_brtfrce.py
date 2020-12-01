import socket
import sys
from termcolor import colored

if len(sys.argv) != 2:
	print(colored("usage script.py <username>", "red"))
	sys.exit(0)


s = socket.socket()
connect = s.connect(('192.168.0.105', 25))

data = s.recv(1024).decode()

command = 'VRFY ' + sys.argv[1] + '\n'

s.send(command.encode())
result = s.recv(1024)
fin_result = result.decode()
valid = '550'
if valid.encode() in result:
	print(colored(sys.argv[1] + " is not a valid user..", "red"))
else:
	print(colored(sys.argv[1] + " is a valid user..", 'blue', attrs=['bold']))
s.close()
