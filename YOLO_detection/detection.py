import cv2
from ultralytics import YOLO

# cargar el modelo de prediccion
modelo = YOLO("train/best2.pt")

#lista de videos a analizar
lista_videos = [
    "Videos/delfines.mp4",
    "Videos/tiburon.mp4",
    "Videos/tortugas.mp4"
]

print("Iniciando análisis secuencial...")
print("Instrucción: Presiona la tecla 'q' para cerrar el video actual y pasar al siguiente.\n")

for ruta_video in lista_videos:
    print(f"--- Reproduciendo: {ruta_video} ---")
    
    #abrir el video actual
    cap = cv2.VideoCapture(ruta_video)
    
    if not cap.isOpened():
        print(f"No se pudo abrir el archivo {ruta_video}")
        continue

    # ciclo de lectura frame por frame
    while cap.isOpened():
        exito, frame = cap.read()
        
        if not exito:
            print(f"Fin natural del video: {ruta_video}")
            break # Termina el video y sale del ciclo while

        # marcar detecciones con fiabilidad de al menos 50%
        resultados = modelo.predict(frame, conf=0.5, verbose=False)
        frame_anotado = resultados[0].plot()

        # mostrar la ventana
        cv2.imshow("Deteccion de Fauna Marina", frame_anotado)

        # presionar q para detener el video y pasar al siguiente
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print(f"Usuario cerró: {ruta_video}")
            break

    # liberar todo
    cap.release()
    cv2.destroyAllWindows()

print("\n¡Todos los videos han sido analizados!")