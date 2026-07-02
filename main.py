import subprocess

# 1. Definimos la base de la red de tu casa (los primeros 3 números)
base_red = "192.168.1."

print("Iniciando escaneo de prueba dinámico...")

# 2. Creamos un bucle que va a contar del 1 al 12
for host in range(1, 12):
    
    # Construimos la IP uniendo la base con el número actual del conteo
    ip_objetivo = base_red + str(host)
    print(f"Probando: {ip_objetivo}")

    # Configuración del comando ping
    comando = ["ping", "-n", "1", "-w", "1000", ip_objetivo]
    
    # Ejecutamos el ping de forma silenciosa
    resultado = subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Evaluamos el resultado
    if resultado.returncode == 0:
        print(f"  ✅ ¡Dispositivo encontrado en {ip_objetivo}!")
    else:
        print(f"  ❌ {ip_objetivo} no respondió.")