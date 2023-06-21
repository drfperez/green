import cv2
import numpy as np

def calcular_percentatge_verd(frame):
    # Convertir la imagen al espacio de color HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definir el rango de color verde en el espacio HSV
    rang_verd_min = np.array([40, 50, 50])     # Valores mínimos para el verde en HSV
    rang_verd_max = np.array([80, 255, 255])   # Valores máximos para el verde en HSV

    # Filtrar los píxeles que se encuentran dentro del rango verde
    mask = cv2.inRange(hsv_frame, rang_verd_min, rang_verd_max)

    # Contar el número de píxeles verdes
    pixels_verds = cv2.countNonZero(mask)

    # Calcular el porcentaje de color verde respecto al total
    total_pixels = frame.shape[0] * frame.shape[1]
    percentatge_verd = (pixels_verds / total_pixels) * 100

    return percentatge_verd, pixels_verds

# Inicializar la lectura del vídeo
video = cv2.VideoCapture('ruta_del_video.mp4')

# Obtener el número total de frames en el video
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Variables para el cálculo de estadísticas
total_pixels_verds = 0
frames_procesados = 0

while True:
    # Leer el frame actual
    ret, frame = video.read()

    if not ret:
        break

    # Calcular el porcentaje de color verde y el número de píxeles verdes
    percentatge_verd, pixels_verds = calcular_percentatge_verd(frame)

    # Mostrar los resultados
    print(f"Percentatge verd: {percentatge_verd:.2f}%")
    print(f"Píxels verds: {pixels_verds}")

    # Actualizar el contador de estadísticas
    total_pixels_verds += pixels_verds
    frames_procesados += 1

    # Mostrar el frame con la máscara de color verde
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    # Esperar por la acción del usuario (presionar 'q' para salir)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Salir si se ha procesado el número de frames deseado (opcional)
    if frames_procesados >= total_frames:
        break

# Calcular las estadísticas finales

