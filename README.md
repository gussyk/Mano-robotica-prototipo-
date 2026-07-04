# Prototipo de Mano Robótica con Visión Artificial 

Este proyecto consiste en el diseño y desarrollo de una mano robótica controlada en tiempo real mediante el rastreo de gestos humanos. Utiliza técnicas de visión artificial para capturar el movimiento de la mano a través de una cámara y traduce esos movimientos en ángulos para servomotores.

## Características
* **Rastreo de alta precisión:** Uso de MediaPipe Hands para detectar 21 puntos clave (landmarks) de la mano.
* **Control en tiempo real:** Comunicación serial de baja latencia entre Python y el microcontrolador.
* **Mapeo de movimiento:** Traducción de la flexión de los dedos a grados de libertad en los servomotores (0° - 180°).

## Tecnologías y Componentes
### Software
* **Python 3.x**
* **OpenCV:** Procesamiento de video y visualización.
* **MediaPipe:** Framework de Google para soluciones de ML aplicadas a la visión.
* **PySerial:** Gestión del puerto serie para comunicación con hardware.

### Hardware (Sugerido)
* **Microcontrolador:** Arduino Uno / ESP32.
* **Actuadores:** 5 Servomotores (MG90S o similares).
* **Estructura:** Impresión 3D / Prototipo mecánico.
* **Alimentación:** Fuente externa de 5V/3A (compartiendo tierra con el microcontrolador).

##  Instalación
1. Clona este repositorio:
   ```bash
   git clone [https://github.com/gussyk/Mano-robotica-prototipo-](https://github.com/gussyk/Mano-robotica-prototipo-)
