import cv2
from playsound import playsound

bd = cv2.barcode_BarcodeDetector_create()
cap = cv2.VideoCapture(0)

detecciones = {}

while True:
    ret, frame = cap.read()
    if ret:
        puntos = bd.detect(frame)
        if len(puntos) > 0:
            for punto in puntos:
                puntos_lista = punto.polygon
                puntos_array = puntos_lista.reshape((-1, 1, 2)).astype(int)
                frame = cv2.polylines(frame, [puntos_array], True, (0, 255, 0), 3)

                ret_bc, decode_info = bd.decode(frame, punto)
                codigo = decode_info[0]

                if codigo in detecciones:
                    detecciones[codigo] += 1
                    if detecciones[codigo] >= 30:
                        print("Detectado:", codigo)
                        playsound('beep.mp3')
                        detecciones = {}
                    else:
                        punto_inicio = punto.rect[0], punto.rect[1]
                        frame = cv2.putText(frame, codigo, punto_inicio, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                else:
                    detecciones[codigo] = 1

    cv2.imshow("Escaner de barras", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
