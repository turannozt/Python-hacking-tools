from ast import arguments
from socket import timeout
from numpy import broadcast
import scapy.all as scapy
import optparse
def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ip",dest="ip_address",help="enter IP address !")
    (user_input,arguments) = parse_object.parse_args()
    if not user_input.ip_address:
        print("Enter IP Address")
        
    return user_input

#1) arp_request
#2) broadcast
#3) response

def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip) #Birinci Aşama Okey
    #scapy.ls(scapy.ARP())

    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    combiend_packet = broadcast_packet/arp_request_packet
    (answered_list,unanswered_list) = scapy.srp(combiend_packet,timeout=1)
    answered_list.summary()

user_ip_address=get_user_input()
scan_my_network(user_ip_address.ip_address)