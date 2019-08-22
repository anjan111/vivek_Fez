# TCP Client
import socket as sk
print "TCP client socket creating"
tcp_cli =sk.socket(sk.AF_INET,sk.SOCK_STREAM)
ip = sk.gethostname()
port = 5005
print "fixing clinet addr : ",(ip,port)
tcp_cli.bind((ip,port))

print "sending the req to ser : "
tcp_cli.connect((ip,5000))

info= tcp_cli.recv(1024)
print "received data :",info," from ",(ip,5000)

info = input("enter sending info : ")
tcp_cli.send(info)
tcp_cli.close()
