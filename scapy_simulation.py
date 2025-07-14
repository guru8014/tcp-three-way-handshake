from scapy.all import *

ip = IP(dst="192.168.1.1")
syn = TCP(dport=80, flags="S", seq=1000)
syn_ack = sr1(ip/syn)
ack = TCP(dport=80, flags="A", seq=syn_ack.ack, ack=syn_ack.seq + 1)
send(ip/ack)