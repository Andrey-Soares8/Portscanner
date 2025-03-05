import tkinter as tk
from tkinter import ttk, messagebox
import socket
from threading import Thread
import random
import time

def get_ip_from_url(url):
    """Resolve o endereço IP de um domínio ou URL."""
    if url.startswith("https://"):
        url = url[len("https://"):]

    if url.startswith("http://"):
        url = url[len("http://"):]

    if "/" in url:
        url = url.split("/")[0]
    
    try:
        return socket.gethostbyname(url)
    except socket.gaierror:
        return None

def scan_port(ip, port, results_text, open_ports, closed_ports):
    """Verifica se uma porta está aberta no IP especificado."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(random.uniform(0.5, 1.5))  # Tempo aleatório para evitar bloqueios
    result = sock.connect_ex((ip, port))
    sock.close()
    
    if result == 0:
        open_ports.append(port)
        msg = f"Port {port} is OPEN\n"
        results_text.insert(tk.END, msg)
    else:
        closed_ports.append(port)
        msg = f"Port {port} is CLOSED\n"
        results_text.insert(tk.END, msg)
    
    results_text.yview(tk.END)  # Rolagem automática para mostrar as portas
    time.sleep(random.uniform(0.1, 0.3))  # Pequena pausa para evitar detecção como ataque

def scan_ports(ip, results_text, quick_scan=False):
    """Escaneia portas principais ou todas as primeiras 1024 portas do IP."""
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 8080]  # Lista de portas mais comuns
    open_ports = []  # Lista para armazenar portas abertas
    closed_ports = []  # Lista para armazenar portas fechadas
    
    def scan_and_update(port):
        scan_port(ip, port, results_text, open_ports, closed_ports)
    
    if quick_scan:
        ports_to_scan = common_ports  # Apenas as portas mais comuns
    else:
        ports_to_scan = list(range(1, 1025))  # Escaneia todas as primeiras 1024 portas
    
    for port in ports_to_scan:
        Thread(target=scan_and_update, args=(port,)).start()
        time.sleep(random.uniform(0.2, 0.5))  # Pequena pausa entre os scans
    
    # Aguarda a conclusão das threads e exibe os resultados
    root.after(5000, lambda: results_text.insert(tk.END, f"\nOpen ports: {open_ports}\nClosed ports: {closed_ports}\n"))

def start_scan(quick_scan=False):
    """Inicia o processo de escaneamento de portas."""
    url = url_entry.get().strip()
    results_text.delete(1.0, tk.END)
    
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return
    
    def resolve_and_scan():
        ip = get_ip_from_url(url)
        if ip:
            results_text.insert(tk.END, f"Scanning {url} ({ip})...\n")
            results_text.update()
            scan_ports(ip, results_text, quick_scan)
            results_text.insert(tk.END, "Scanning complete.\n")
        else:
            results_text.insert(tk.END, f"Could not resolve URL: {url}\n")
        results_text.update()
    
    Thread(target=resolve_and_scan).start()

# Interface gráfica
root = tk.Tk()
root.title("Port Scanner")
root.geometry("400x450")

frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

url_label = ttk.Label(frame, text="URL:")
url_label.pack(anchor=tk.W)

url_entry = ttk.Entry(frame, width=40)
url_entry.pack(fill=tk.X, padx=5, pady=5)

scan_full_button = ttk.Button(frame, text="Full Scan", command=lambda: start_scan(False))
scan_full_button.pack(pady=5)

scan_quick_button = ttk.Button(frame, text="Quick Scan", command=lambda: start_scan(True))
scan_quick_button.pack(pady=5)

results_frame = ttk.Frame(frame)
results_frame.pack(fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(results_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

results_text = tk.Text(results_frame, width=50, height=15, yscrollcommand=scrollbar.set)
results_text.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=results_text.yview)

root.mainloop()
