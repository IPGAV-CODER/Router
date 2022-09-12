import random
import time

def RESTART():
	print("O router está sendo desligado...")
	time.sleep(5)
	quit()

def REQUESTS():
	# Listar todas as requests -  que ficam num .txt
	COMMAND()

def CONFIG_REQUESTS(MODE):
	print("Reading requests...")
	time.sleep(5)
	if MODE == "Auto":
		C012A = open("21BCE.txt","r")
		C012A_INFO = C012A.readline()
		if "ETH" in C012A_INFO:
			C012A_SPLIT = C012A_INFO.split("#")
			IP_REQUEST = C012A_SPLIT[3]
			MODE_REQUEST = C012A_SPLIT[4]
			TYPE_REQUEST = C012A_SPLIT[5]
			C014A = open("C0AAAB.txt","w")
			NEW_IP = str(random.randint(100000000, 999999999))
			C014A.write(NEW_IP)
			C014A.close()
			print("Setting...")
			time.sleep(10)
			C017A = open("21C99.txt","r")
			C017A_INFO = C017A.readline()
			C017A_SPLIT = C017A_INFO.split("#")
			if C017A_SPLIT[0] == C012A_SPLIT[3]:
				if C017A_SPLIT[1] == NEW_IP:
					print("Conectado com " + IP_REQUEST)
					print("IP referente - " + NEW_IP)
					COMMAND()
				else:
					print("Erro de compatibilidade de IP. Solicite uma nova request.")
					RESTART()
			else:
				print("Request inesperado. Solicite uma nova request.")
				RESTART()
	elif MODE == "Manual":
		print("MODO MANUAL - Não funcional ainda. \n\n")
		COMMAND()
	else:
		print("Error 101")
		COMMAND()

def CONFIG_GATEWAY():
	F0015 = input("MASK: ")
	F0017 = input("Gateway: ")
	router_config = open("A00EF13.txt","w")
	router_config.write("Mask: " + F0015 + "\nGateway: " + F0017)
	router_config.close()
	F0020A = "Auto"
	CONFIG_REQUESTS(F0020A)

def COMMAND():
	CMD = input("CMD> ")
	exec(CMD)

COMMAND()
