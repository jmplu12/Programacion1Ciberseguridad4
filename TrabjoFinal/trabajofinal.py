import ipaddress  # Para validar direcciones IP

# Función para leer una IP válida
def leer_ip(mensaje):
    while True:
        ip = input(mensaje).strip()
        try:
            # Valida IPv4 o IPv6; si no es válida lanza excepción
            ipaddress.ip_address(ip)
            return ip
        except ValueError:
            print("IP no válida. Intenta de nuevo.")

# Algoritmo Firewall en Python con validaciones

bloqueadas = []
paquetes = []

# Entrada de datos: IPs bloqueadas (máximo 3), sin duplicados y formato válido
for i in range(1, 4):
    while True:
        ip = leer_ip(f"Ingrese IP bloqueada #{i}: ")
        if ip in bloqueadas:
            print("Esa IP ya está bloqueada. Ingresa una diferente.")
        else:
            bloqueadas.append(ip)
            break

# Entrada de datos: características de cada paquete entrante
for i in range(1, 4):
    print(f"\nPaquete #{i}")
    ip_origen = leer_ip("Ingrese IP de origen: ")

    # Puerto: número entre 1 y 65535
    while True:
        puerto_destino = input("Ingrese puerto destino (1-65535): ").strip()
        if puerto_destino.isdigit():
            puerto_int = int(puerto_destino)
            if 1 <= puerto_int <= 65535:
                break
        print("Puerto inválido. Debe ser un número entre 1 y 65535.")

    protocolo = input("Ingrese protocolo (por ejemplo TCP/UDP): ").strip().upper()
    paquetes.append([ip_origen, puerto_int, protocolo])

# Proceso de validación: se verifica si la IP está en la lista bloqueada
for i, paquete in enumerate(paquetes, start=1):
    ip_origen = paquete[0]
    bloqueado = ip_origen in bloqueadas

    if bloqueado:
        print(f"Paquete {i}: BLOQUEADO (IP: {ip_origen})")
    else:
        print(f"Paquete {i}: PERMITIDO (IP: {ip_origen})")
