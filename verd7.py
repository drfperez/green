import cv2
import pafy

def calcular_percentatge_verd(frame, rang_verd_min, rang_verd_max):
    # Filtrar los píxeles que se encuentran dentro del rango verde
    mask = cv2.inRange(frame, rang_verd_min, rang_verd_max)
    
    # Contar el número de píxeles verdes
    pixels_verds = cv2.countNonZero(mask)
    
    # Calcular el porcentaje de color verde respecto al total
    total_pixels = frame.shape[0] * frame.shape[1]
    percentatge_verd = (pixels_verds / total_pixels) * 100
    
    return percentatge_verd, pixels_verds

# Definir el rango de color verde en el espacio RGB
rang_verd_min = (0, 100, 0)      # Valores mínimos para el verde en RGB
rang_verd_max = (100, 255, 100)  # Valores máximos para el verde en RGB

# Obtener el enlace al video de YouTube en streaming
video_url = "https://www.youtube.com/watch?v=<your_video_id>"
video = pafy.new(video_url)
best_stream = video.getbest(preftype="mp4")

# Inicializar la lectura del vídeo en streaming
cap = cv2.VideoCapture()
cap.open(best_stream.url)

while True:
    # Leer el frame actual
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Calcular el porcentaje de color verde y el número de píxeles verdes
    percentatge_verd, pixels_verds = calcular_percentatge_verd(frame, rang_verd_min, rang_verd_max)
    
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
cap.release()
cv2.destroyAllWindows()

