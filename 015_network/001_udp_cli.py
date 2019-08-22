# UDP Client
import socket as sk
print "UDP client socket creating"
udp_cli =sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
ip = sk.gethostname()
port = 5005
print "fixing clinet addr : ",(ip,port)
udp_cli.bind((ip,port))
info,addr = udp_cli.recvfrom(1024)
print "received data :",info," from ",addr

info = input("enter sending info : ")
udp_cli.sendto(info,(ip,5000))
udp_cli.close()
