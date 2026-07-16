# 🔍 Ping Sweeper - Local Network Scanner

Este es un script de automatización en Python diseñado para auditar la seguridad de una red local. Funciona enviando paquetes ICMP (pings) de forma consecutiva a un rango de direcciones IP específicas y resolviendo los nombres de los dispositivos activos conectados (Reverse DNS).

## 🚀 Características
* **Escaneo automatizado:** Analiza dinámicamente un rango completo de subred.
* **Resolución de nombres:** Identifica el fabricante o nombre del dispositivo (`socket`).
* **Modo Silencioso:** Filtra las direcciones inactivas para una lectura limpia.
* **Reporte Automático:** Exporta los resultados detallados a un archivo físico (`reporte_red.txt`) con fecha y hora.

## 🛠️ Tecnologías utilizadas
* **Python 3**
* Librería `subprocess` (para interactuar con comandos del sistema).
* Librería `socket` (para traducción de IPs a nombres de host).

## 📋 Requisitos
Solo requiere tener Python instalado en tu máquina (compatible con Windows y Linux).

## 💾 Ejemplo de Reporte Generado
```text
==================================================
      REPORTE DE SEGURIDAD - RED LOCAL CASERA     
==================================================
Fecha y Hora del Análisis: 2026-07-16 12:00:00
Rango de IPs analizado: 192.168.1.1 al 192.168.1.24
--------------------------------------------------

✅ ¡Dispositivo ENCONTRADO! -> 192.168.1.1 | Nombre: router.home
✅ ¡Dispositivo ENCONTRADO! -> 192.168.1.15 | Nombre: iPhone-de-Juan

--------------------------------------------------

=== Escaneo Finalizado ===
📊 Total de dispositivos activos detectados: 2
==================================================
