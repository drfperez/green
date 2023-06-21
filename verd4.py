
import cv2
import numpy as np

def calcular_percentatge_verd(frame):
    # Definir el rango de color verde en el espacio RGB
    rang_verd_min = np.array([0, 100, 0])      # Valores mínimos para el verde en RGB
    rang_verd_max = np.array([100, 255, 100])  # Valores máximos para el verde en RGB
    
    # Filtrar los píxeles que se encuentran dentro del rango verde
    mask = cv2.inRange(frame, rang_verd_min, rang_verd_max)
    
    # Contar el número de píxeles verdes
    pixels_verds = cv2.countNonZero(mask)
    
    # Calcular el porcentaje de color verde respecto al total
    total_pixels = frame.shape[0] * frame.shape[1]
    percentatge_verd = (pixels_verds / total_pixels) * 100
    
    return percentatge_verd, pixels_verds

# Inicializar la lectura del vídeo
video = cv2.VideoCapture('ruta_del_video.mp4')

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
    
    # Filtrar los píxeles que se encuentran dentro del rango verde
    mask = cv2.inRange(frame, rang_verd_min, rang_verd_max)
    
    # Mostrar el frame con la máscara de color verde
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    
    
    # Esperar por la acción del usuario (presionar 'q' para salir)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
video.release()
cv2.destroyAllWindows()

