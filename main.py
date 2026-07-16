import subprocess
import socket
from datetime import datetime  # Para registrar la fecha y hora del escaneo

base_red = "192.168.1."  # Recuerda usar tu base real
dispositivos_encontrados = 0
resultados_lista = []  # Aquí guardaremos temporalmente los hallazgos

print("🔍 Iniciando escaneo definitivo de la red local...")
print("Por favor, espera un momento...\n")

# Escaneamos el rango (puedes ajustarlo si lo deseas)
for host in range(1, 21): 
    ip_objetivo = base_red + str(host)
    
    comando = ["ping", "-n", "1", "-w", "1000", ip_objetivo]
    resultado = subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if resultado.returncode == 0:
        try:
            nombre_host, _, _ = socket.gethostbyaddr(ip_objetivo)
        except (socket.herror, socket.gaierror):
            nombre_host = "Nombre desconocido"
            
        linea = f"✅ ¡Dispositivo ENCONTRADO! -> {ip_objetivo} | Nombre: {nombre_host}"
        print(linea)
        resultados_lista.append(linea)  # Guardamos la línea para el archivo
        dispositivos_encontrados += 1

resumen = f"\n=== Escaneo Finalizado ===\n📊 Total de dispositivos activos detectados: {dispositivos_encontrados}"
print(resumen)

# --- NUEVO: GUARDAR EN ARCHIVO DE TEXTO ---
fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("reporte_red.txt", "w", encoding="utf-8") as archivo:
    archivo.write("==================================================\n")
    archivo.write("      REPORTE DE SEGURIDAD - RED LOCAL CASERA     \n")
    archivo.write("==================================================\n")
    archivo.write(f"Fecha y Hora del Análisis: {fecha_actual}\n")
    archivo.write(f"Rango de IPs analizado: {base_red}1 al {base_red}24\n")
    archivo.write("--------------------------------------------------\n\n")
    
    # Escribimos cada dispositivo encontrado
    for dispositivo in resultados_lista:
        archivo.write(dispositivo + "\n")
        
    archivo.write("\n--------------------------------------------------\n")
    archivo.write(resumen + "\n")
    archivo.write("==================================================\n")

print("\n💾 Reporte guardado con éxito en 'reporte_red.txt'")