banner = r"""
                ███╗   ██╗███████╗ ██████╗                  
                ████╗  ██║██╔════╝██╔═══██╗                 
                ██╔██╗ ██║███████╗██║   ██║                 
                ██║╚██╗██║╚════██║██║   ██║                 
                ██║ ╚████║███████║╚██████╔╝                 
                ╚═╝  ╚═══╝╚══════╝ ╚═════╝                  
                                                            
███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
"""

print(banner)

import socket
import time
from scapy.all import *


def scan_ports(host, start_port, end_port):
    """
    Escaneia um range de portas em um host de destino para verificar se há portas abertas.

    Args:
    host (str): O endereço IP ou nome de domínio do host de destino.
    start_port (int): A primeira porta a ser escaneada.
    end_port (int): A última porta a ser escaneada.

Retorna:
    Uma lista de portas abertas no host de destino e a duração do escaneamento em segundos.
 """
    ip = get_ip(host)
    open_ports = []
    start_time = time.time()
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    end_time = time.time()
    duration = end_time - start_time
    return open_ports, duration


def get_domain(ip):
    """
    Converte o endereço IP para um domínio.

    Args:
        ip (str): O IP a ser convertido.

    Returns:
       O nome de domínio associado ao endereço IP ou o endereço IP original se nenhum nome de domínio for encontrado.
       """
    try:
        domain = socket.gethostbyaddr(ip)[0]
    except socket.herror:
        domain = ip
    return domain


def get_ip(domain):
    """
    Converta um nome de domínio em um endereço IP.

     Args:
         domain (str): O nome de domínio para converter.

     Retorna:
         O endereço IP associado ao nome de domínio ou o nome de domínio original se nenhum endereço IP for encontrado.
    """
    try:
        ip = socket.gethostbyname(domain)
    except socket.gaierror:
        ip = domain
    return ip


# Solicite ao usuário o endereço IP do host de destino ou o nome de domínio e o intervalo de portas a serem verificados.
host = input("Insira o endereço IP do host de destino ou o nome de domínio: ")
start_port = int(input("Digite o número da porta inicial: "))
end_port = int(input("Digite o número da porta final: "))

# Examine o intervalo especificado de portas no host de destino e imprima a lista de portas abertas, se houver.
print("Examinando porta {} até {} no host {}...".format(start_port, end_port, host))
open_ports, duration = scan_ports(host, start_port, end_port)
if open_ports:
    print("Portas abertas: ", open_ports)
else:
    print("Sem portas abertas.")

# Mostra a duração da verificação em minutos e segundos, se exceder 60 segundos.
if duration < 60:
    print("Duração da verificação: {:.2f} segundos".format(duration))
else:
    minutes = int(duration // 60)
    seconds = duration % 60
    print("Duração da verificação: {} minutos(s) {:.2f} segundos".format(minutes, seconds))

# Converta o endereço IP ou nome de domínio em seu tipo oposto e mostra o resultado.
if "." in host:
    print("Nome de domínio: ", get_domain(host))
else:
    print("Endereço IP: ", get_ip(host))



# Definir uma função para enviar uma solicitação de eco ICMP e analisar a resposta
def detect_os(ip_address):
    # Envie uma solicitação de eco ICMP para o host remoto
    icmp_request = IP(dst=ip_address)/ICMP()
    icmp_reply = sr1(icmp_request, timeout=2, verbose=0)

    # Extraia o valor TTL da resposta ICMP
    ttl = icmp_reply.ttl

    # Use o valor TTL para determinar o sistema operacional
    if ttl <= 64:
        return "OS: Linux"
    elif ttl <= 128:
        return "OS: Windows"
    else:
        return "OS não reconhecida"

# Chamar a função detect_os() com o endereço IP do host remoto
os = detect_os('127.0.0.1')

# Mostrar o sistema operacional detectado
print(os)


