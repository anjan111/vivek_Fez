# TCP server
import socket as sk
print "TCP Server socket creating"
tcp_ser =sk.socket(sk.AF_INET,sk.SOCK_STREAM)
ip = sk.gethostname()
port = 5000
print "fixing server addr : ",(ip,port)
tcp_ser.bind((ip,port))
print "fixing 1 client"
tcp_ser.listen(1)
print "waiting for cooncetion"
con,addr = tcp_ser.accept()
print "server is connceted to : ",addr
info = input("enter sending info : ")
con.send(info)
info= con.recv(1024)
print "received data :",info," from ",addr
tcp_ser.close()
