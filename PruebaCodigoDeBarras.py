import cv2

# Crea un objeto detector de códigos de barras
detector = cv2.barcode_BarcodeDetector()

# Carga la imagen
imagen = cv2.imread('codigo.png')

# Detecta y decodifica el código de barras
retval, decoded_info, points = detector.detectAndDecode(imagen)

if retval:
    # Dibuja un polígono alrededor del código de barras detectado
    for point in points:
        cv2.polylines(imagen, point, True, (0, 255, 0), 2)

    # Muestra los datos decodificados y la imagen
    print("Datos del código de barras: ", decoded_info)
    cv2.imshow('Imagen', imagen)
    cv2.waitKey(0)
else:
    print('No se ha detectado ningún código de barras')