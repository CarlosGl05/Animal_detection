import cv2
import numpy as np

def procesar_animales(nombre_archivo):
    cap = cv2.VideoCapture(nombre_archivo)
    
    window_name = f"Deteccion: {nombre_archivo}"


    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 480))
        
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        
        lower_animal = np.array([0, 0, 0])
        upper_animal = np.array([180, 255, 130]) 
        
        mask = cv2.inRange(hsv, lower_animal, upper_animal)

        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 800:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(frame, "Objeto Detectado", (x, y - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        cv2.imshow(window_name, frame)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyWindow(window_name)

videos = ["tiburon.mp4", "tortugas.mp4", "delfines.mp4"]

for v in videos:
    procesar_animales(v)

cv2.destroyAllWindows()