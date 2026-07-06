import subprocess

base_red = "192.168.1."
# Creamos una variable para contar los dispositivos encontrados
dispositivos_encontrados = 0

print("🔍 Iniciando escaneo silencioso de la red local...")
print("Por favor, espera un momento...\n")

# Ampliamos un poco el rango (por ejemplo, del 1 al 20 para probar)
for host in range(1, 21):
    ip_objetivo = base_red + str(host)
    
    comando = ["ping", "-n", "1", "-w", "1000", ip_objetivo]
    resultado = subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if resultado.returncode == 0:
        print(f"✅ ¡Dispositivo ENCONTRADO! -> {ip_objetivo}")
        # Si encuentra uno, le sumamos 1 al contador
        dispositivos_encontrados += 1
    # Eliminamos el 'else' para que no imprima nada si la IP está inactiva

# Al salir del bucle, mostramos el resumen
print("\n=== Escaneo Finalizado ===")
print(f"📊 Total de dispositivos activos detectados: {dispositivos_encontrados}")