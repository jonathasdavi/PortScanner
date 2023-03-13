import tkinter as tk
from tkinter import messagebox
import socket
import time
from scapy.all import *

class PortScanner(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NSO Scanner")
        self.geometry("700x400")
        self.configure(bg="black")

        # Componentes da interface gráfica
        tk.Label(self, text="Endereço IP ou nome de domínio:", font=("Arial", 12), bg="black", fg="#00FF00").pack(pady=10)
        self.host_entry = tk.Entry(self, width=30, font=("Arial", 12))
        self.host_entry.pack()

        tk.Label(self, text="Intervalo de portas:", font=("Arial", 12), bg="black", fg="#00FF00").pack(pady=(20, 10))

        port_frame = tk.Frame(self, bg="black")
        port_frame.pack()

        self.start_port_entry = tk.Entry(port_frame, width=10, font=("Arial", 12))
        self.start_port_entry.pack(side=tk.LEFT, padx=10)

        tk.Label(port_frame, text="-", font=("Arial", 12), bg="black", fg="#00FF00").pack(side=tk.LEFT)

        self.end_port_entry = tk.Entry(port_frame, width=10, font=("Arial", 12))
        self.end_port_entry.pack(side=tk.LEFT, padx=10)

        tk.Button(self, text="Verificar", command=self.scan_ports, font=("Arial", 12), bg="#00FF00", fg="black").pack(padx=10, pady=15)

        tk.Label(self, text="Resultado:", font=("Arial", 12), bg="black", fg="#00FF00").pack(pady=10)

        self.result_text = tk.Text(self, height=10, state="disabled", font=("Arial", 12))
        self.result_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def scan_ports(self):
        # Obter o endereço IP ou nome de domínio do alvo
        host = self.host_entry.get()

        # Obter o intervalo de portas a serem verificadas
        start_port = int(self.start_port_entry.get())
        end_port = int(self.end_port_entry.get())

        # Verificar as portas uma por uma
        open_ports = []
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
            sock.close()

        # Exibir os resultados na caixa de texto
        if len(open_ports) > 0:
            self.result_text.config(state="normal")
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Portas abertas: {open_ports}")
            self.result_text.config(state="disabled")
        else:
            messagebox.showinfo("Port Scanner", "Nenhuma porta aberta encontrada.")

app = PortScanner()
app.mainloop()
