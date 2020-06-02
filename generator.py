def read(): #read ip.txt (first line)
     read=open("ip.txt", "r") # put attacker ip in ip.txt
     data=read.read()
     read.close()
     return data
temp=read()

for numero in temp:
    cryptlist=["$","#","*","-","@","%","?","!","+"]
    if numero != "." :
        numero=cryptlist[int(numero)-1]
        ip_re+=numero
    else:
        ip_re+=numero
write_temp=open("ip.txt","w")
write_temp.write(ip_re)
write_temp.close()
