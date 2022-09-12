import random
import time

def CHECK_IP(OLD_IP):
	C014A = open("C0AAAB.txt","r")
	IP = C014A.readline()
	C014A.close()
	C017A = open("21C99.txt","w")
	C017A.write(OLD_IP + "#" + IP)
	C017A.close()
	print("Seu novo IP - " + IP)
	COMMAND()

def ETH(ADDRESS, MODE, TYPE):
	PACK_1 = "Connection: #ETH#FROM#" + ADDRESS + "#"+ MODE +"#" + TYPE
	C012A = open("21BCE.txt","w")
	C012A.write(PACK_1 + "\n")
	C012A.close()
	print("Wait a moment...")
	time.sleep(10)
	CHECK_IP(ADDRESS)

def IP():
	# Solicitando ao Roteador um IP
	IP_TEMP = "100000001"
	ETH(IP_TEMP, "REQ", "IPV4")
	
def COMMAND():
	CMD = input("CMD> ")
	exec(CMD)

COMMAND()
