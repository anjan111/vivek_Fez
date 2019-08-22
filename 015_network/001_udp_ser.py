# UDP server
import socket as sk
print "UDP Server socket creating"
udp_ser =sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
ip = sk.gethostname()
port = 5000
print "fixing server addr : ",(ip,port)
udp_ser.bind((ip,port))
info = input("enter sending info : ")
udp_ser.sendto(info,(ip,5005))
info,addr = udp_ser.recvfrom(1024)
print "received data :",info," from ",addr
udp_ser.close()
