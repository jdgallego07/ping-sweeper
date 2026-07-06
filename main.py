import subprocess
import socket  # 1. Importamos la nueva librería de red

base_red = "192.168.1."  # Recuerda usar tu base real
dispositivos_encontrados = 0

print("🔍 Iniciando escaneo con resolución de nombres...")
print("Por favor, espera un momento...\n")

# Usa el rango que configuraste anteriormente donde están tus dispositivos
for host in range(1, 21): 
    ip_objetivo = base_red + str(host)
    
    comando = ["ping", "-n", "1", "-w", "1000", ip_objetivo]
    resultado = subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if resultado.returncode == 0:
        # 2. Intentamos obtener el nombre del dispositivo
        try:
            # gethostbyaddr nos devuelve una tupla, solo nos interesa el primer elemento (el nombre)
            nombre_host, _, _ = socket.gethostbyaddr(ip_objetivo)
        except (socket.herror, socket.gaierror):
            # Si el dispositivo no revela su nombre o el router no lo sabe
            nombre_host = "Nombre desconocido"
            
        # 3. Mostramos la IP junto a su nombre
        print(f"✅ ¡Dispositivo ENCONTRADO! -> {ip_objetivo} | Nombre: {nombre_host}")
        dispositivos_encontrados += 1

print("\n=== Escaneo Finalizado ===")
print(f"📊 Total de dispositivos activos detectados: {dispositivos_encontrados}")