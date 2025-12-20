import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# --- CONEXIÓN A LA BASE DE DATOS ---
def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="firewall_db"
    )

class FirewallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Firewall Básico")
        self.root.geometry("600x500")

        # Variables
        self.ip_var = tk.StringVar()
        self.puerto_var = tk.StringVar()
        self.protocolo_var = tk.StringVar(value="TCP")

        # UI - Formulario
        tk.Label(root, text="SIMULADOR DE FIREWALL", font=("Arial", 14, "bold")).pack(pady=10)
        
        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Label(frame, text="IP Origen:").grid(row=0, column=0)
        tk.Entry(frame, textvariable=self.ip_var).grid(row=0, column=1)

        tk.Label(frame, text="Puerto:").grid(row=1, column=0)
        tk.Entry(frame, textvariable=self.puerto_var).grid(row=1, column=1)

        tk.Label(frame, text="Protocolo:").grid(row=2, column=0)
        ttk.Combobox(frame, textvariable=self.protocolo_var, values=["TCP", "UDP", "ICMP"]).grid(row=2, column=1)

        tk.Button(root, text="Registrar Paquete", command=self.registrar_paquete, bg="blue", fg="white").pack(pady=10)

        # Tabla de Registros
        self.tabla = ttk.Treeview(root, columns=("IP", "Puerto", "Protocolo", "Estado"), show='headings')
        self.tabla.heading("IP", text="IP Origen")
        self.tabla.heading("Puerto", text="Puerto")
        self.tabla.heading("Protocolo", text="Protocolo")
        self.tabla.heading("Estado", text="Estado")
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)

        self.mostrar_registros()

    def obtener_ips_bloqueadas(self):
        db = conectar_db()
        cursor = db.cursor()
        cursor.execute("SELECT ip FROM ips_bloqueadas")
        # Esto es un vector (lista) de IPs
        lista = [fila[0] for fila in cursor.fetchall()]
        db.close()
        return lista

    def registrar_paquete(self):
        ip = self.ip_var.get()
        puerto = self.puerto_var.get()
        proto = self.protocolo_var.get()

        if not ip or not puerto:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        # Lógica de Validación (Condicionales y Vectores)
        bloqueadas = self.obtener_ips_bloqueadas()
        
        if ip in bloqueadas:
            estado = "BLOQUEADO"
            self.generar_alerta(ip)
        else:
            estado = "PERMITIDO"

        # Guardar en Matriz/Base de datos
        try:
            db = conectar_db()
            cursor = db.cursor()
            query = "INSERT INTO registros (ip_origen, puerto, protocolo, estado) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (ip, puerto, proto, estado))
            db.commit()
            db.close()
            self.mostrar_registros()
        except Exception as e:
            messagebox.showerror("Error DB", str(e))

    def mostrar_registros(self):
        # Limpiar tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        db = conectar_db()
        cursor = db.cursor()
        cursor.execute("SELECT ip_origen, puerto, protocolo, estado FROM registros ORDER BY fecha DESC")
        # Matriz de registros
        for fila in cursor.fetchall():
            self.tabla.insert("", "end", values=fila)
        db.close()

    def generar_alerta(self, ip):
        messagebox.showerror("ALERTA DE SEGURIDAD", f"Intento de acceso detectado desde IP BLOQUEADA: {ip}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FirewallApp(root)
    root.mainloop()