import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if ret:
            barcodes = find_barcodes(frame)
            frame = draw_barcodes(frame, barcodes)
            colors = find_colors(frame)
            frame = draw_colors(frame, colors)

            cv2.imshow("Tracking", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

def find_barcodes(frame):
    barcode_detector = cv2.barcode.BarcodeDetector()
    (ret_bc, decode, puntos) = barcode_detector.detectAndDecode(frame)

    barcodes = {}
    if ret_bc:
        for codigo, punto in zip(decode, puntos):
            barcodes[codigo] = punto

    return barcodes

def draw_barcodes(frame, barcodes):
    for codigo, punto in barcodes.items():
        frame = cv2.polylines(frame,np.int32([punto.astype(int)]),True,(0,255,0),3)
        frame = cv2.putText(frame,codigo,punto[1].astype(int),
                            cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2,cv2.LINE_AA)

    return frame

def find_colors(frame):
    # Definir el rango de colores que desea rastrear aquí
    # Por ejemplo, rojo oscuro
    lower_color = np.array([0, 0, 200])
    upper_color = np.array([150, 150, 255])

    # Convertir la imagen de BGR a HSV
    hsv = cv2.cvtagen de BColor(GRframe, cv a H2.SVCOLOR
   _B hsvGR2 = cvHSV2)
.cv
   t #Color( Aplicframear el fil,tro cv2 de col.COLores
OR   _BGR2 maskH = cvSV)2.
in
   Range( #hsv Utilizar, lower la fun_colorción, upper de má_colorsc)
ara en
 la    # imagen Aplic para extraar dileratación el color y er desosióneado para elimin
   ar ru maskido
 = cv    kernel2 = np.inRange.ones(((h5, sv,5 lower), np_color.uint, upper8)
_    maskcolor) = cv
   2. resdil = cvate(2.mask,bitwise kernel,_and iterations=(1)frame,
    frame, mask = cv mask=2.mask)erode

(mask    #, kernel, Encontr iterations=ar los1) contorn

   os del # En objetocontrar
    contornos contours en la, _ másc = cvara
   2. contoursfindCont, _ours( = cv2mask,.find cv2.ContoursRETR(mask_T, cvREE,2. cv2RETR_.CHEXTERNAAL, cv2.CHAIN_APPROX_IN_SIMPAPPROLE)X

   _SIMP return contoursLE)



def draw_    colorscolors( = {}frame, cont
   ours): for c
    fornt in contour in contours contours::

        area        M = cv = cv2.cont2.mourArea(omentscontour)(cnt
       )
 if area >        if 10 M["m00:00 # El"] !=iminar objet 0os peque:
ños
                       cX x, y = int, w,(M h = cv["m12.bound0"]ingRect( / Mcontour)["m
            cv002.rect"])
angle(frame            cY, (x = int, y), ((M["x + wm0, y + h1"] /), (0 M[", m00"])255
           , 0 colors[(c), 2X,)

 cY)]    return frame = (

iflower_color __name__, upper_ == "__color)main__":

   
    main return colors()