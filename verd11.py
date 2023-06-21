import cv2
import numpy as np

def calcular_percentatge_verd(frame, rang_verd_min, rang_verd_max):
    # Convertir la imagen al espacio de color HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Filtrar los píxeles que se encuentran dentro del rango verde en HSV
    mask = cv2.inRange(hsv_frame, rang_verd_min, rang_verd_max)
    
    # Contar el número de píxeles verdes
    pixels_verds = cv2.countNonZero(mask)
    
    # Calcular el porcentaje de color verde respecto al total
    total_pixels = frame.shape[0] * frame.shape[1]
    percentatge_verd = (pixels_verds / total_pixels) * 100
    
    return percentatge_verd, pixels_verds

# Definir el rango de color verde en el espacio HSV
rang_verd_min = np.array([35, 50, 50])      # Valores mínimos para el verde en HSV
rang_verd_max = np.array([85, 255, 255])  # Valores máximos para el verde en HSV

# Inicializar la lectura del vídeo
video = cv2.VideoCapture('ruta_del_video.mp4')

percentatges_verds = []  # Lista para almacenar los porcentajes de verde
pixels_verds_total = 0   # Contador para el total de píxeles verdes

while True:
    # Leer el frame actual
    ret, frame = video.read()
    
    if not ret:
        break
    
    # Calcular el porcentaje de color verde y el número de píxeles verdes
    percentatge_verd, pixels_verds = calcular_percentatge_verd(frame, rang_verd_min, rang_verd_max)
    
    # Almacenar el porcentaje de verde en la lista
    percentatges_verds.append(percentatge_verd)
    
    # Sumar los píxeles verdes al contador total
    pixels_verds_total += pixels_verds
    
    # Mostrar los resultados
    print(f"Percentatge verd: {percentatge_verd:.2f}%")
    print(f"Píxels verds: {pixels_verds}")
    
    # Filtrar los píxeles que se encuentran dentro del rango verde en HSV
    mask = cv2.inRange(frame, rang_verd_min, rang_verd_max)
    
    # Mostrar el frame con la máscara de color verde
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    
    # Esperar por la acción del usuario (presionar 'q' para salir)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Calcular las estadísticas resumidas
num_frames = len(percentatges_verds)
percentatge_verd_promig = np.mean(percentatges_verds)
pixels_verds_promig = pixels_verds_total / num_frames

# Mostrar las estadísticas resumidas
print("Estadísticas resumidas:")
print(f"Número de frames: {num_frames}")
print(f"Percentatge verd promig: {percentatge_verd_promig:.2f}%")
print(f"Píxels verds promig: {pixels_verds_promig:.2f}")

# Liberar recursos
video.release()
cv2.destroyAllWindows()
